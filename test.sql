SELECT
  campaign.tenant_id,
  tmp.poi_id,
   1 as is_starter,
   -1 as coupon_template_id,
   campaign.campaign_id as campaign_id,
   campaign.campaign_name as campaign_name,
   campaign.campaign_status as campaign_status,
  campaign.campaign_type,
  campaign.campaign_restrict_type,
   tmp.stat_date as stat_date,
   tmp.offered_coupon_cnt as offered_coupon_cnt,
   tmp.verified_coupon_cnt as verified_coupon_cnt,
   tmp.order_amt as order_amt,
   tmp.order_cnt as order_cnt,
   tmp.avg_order_amt as avg_order_amt,
   0 as coupon_amt,
   0 as consume_asset_amt,
   0 as consume_cash_amt,
   0 as consume_point_amt,
   tmp.biz_promotion_amt as biz_promotion_amt,
   0 as biz_promotion_revenue --23379094
FROM (
       select COALESCE(sender.stat_date, consumer.stat_date) as stat_date,
              COALESCE(sender.offered_coupon_cnt, 0) as offered_coupon_cnt,
              COALESCE(consumer.verified_coupon_cnt, 0) as verified_coupon_cnt,
              COALESCE(consumer.order_amt, 0) as order_amt,
              COALESCE(consumer.order_cnt, 0) as order_cnt,
              COALESCE(consumer.avg_order_amt, 0) as avg_order_amt,
              COALESCE(sender.campaign_id, consumer.campaign_id) as campaign_id,
              COALESCE(sender.source, consumer.source) as source,
              COALESCE(consumer.biz_promotion_amt, 0) as biz_promotion_amt,
              COALESCE(sender.poi_id, consumer.poi_id) as poi_id
       FROM (
              select
                count(t1.coupon_id) as offered_coupon_cnt,
                t1.campaign_id as campaign_id,
                t1.`source` as `source`,
                t1.stat_date as stat_date,
                if(`from` = 'dp', t2.mt_main_poi_id, t1.poi_id) as poi_id
              from
                (select
                   coupon_id,
                   campaign_id,
                   source,
                   sent_date as stat_date,
                   poi_id,
                   `from`
                 FROM mart_crm.dwd_crm_red_packet
                 WHERE
                 partition_date = '2018-01-08'
                 AND sent_date = '2018-01-08'
                )t1
                left OUTER JOIN
                (
                  select
                    poi_id, --点评的poi_id
                    mt_main_poi_id --美团的poi_id
                  from
                    mart_catering.dim_common_xmd_poi_ss
                  WHERE
                    partition_chain = 'dp'
                    and partition_date = '2018-01-08'
                )t2
                  on t1.poi_id = t2.poi_id
              group by t1.campaign_id,
                t1.`source`,
                t1.stat_date,
                if(`from` = 'dp', t2.mt_main_poi_id, t1.poi_id)
            )sender
       LEFT OUTER JOIN(
       select campaign_id,
       case when `source` = 'waimai' then sum(waimaiOrder.order_amt) else sum(opening.order_amount) / 100.00 end as order_amt,
       count(opening.coupon_id) as verified_coupon_cnt,
       count(opening.order_id) as order_cnt,
       `source`,
       sum(coupon_value) / 100.00 as biz_promotion_amt,
       case when `source` = 'waimai' then sum(waimaiOrder.order_amt) / count(opening.order_id)
       else sum(order_amount) / 100.00 / count(opening.order_id) end as avg_order_amt,
       partition_date as stat_date,
       offer.poi_id
      FROM (
       select *
       from mart_crm.dwd_crm_red_packet_open
       WHERE
       partition_date = '2018-01-08'
      )opening
       join (
       select coupon_id,
       if(`from` = 'dp', t2.mt_main_poi_id, t1.poi_id) as poi_id
      from
       (
       select coupon_id,
       poi_id,
       `from`
       from mart_crm.dwd_crm_red_packet
       WHERE partition_date = '2018-01-08'
       )t1
        left OUTER JOIN
       (
       select
       poi_id,
       mt_main_poi_id
       from
       mart_catering.dim_common_xmd_poi_ss
       WHERE
       partition_chain = 'dp' and partition_date= '2018-01-08'
       )t2
        on t1.poi_id = t2.poi_id
      )offer
       on opening.coupon_id = offer.coupon_id
       LEFT OUTER JOIN (
      select
      order_id,
      order_amt
      from
      mart_crm.dwd_crm_xmd_order_waimai_daily
      WHERE


      partition_date = '2018-01-08'
                       )waimaiOrder
                        on opening.order_id = waimaiOrder.order_id
                        group by campaign_id,
                              source,
                              partition_date,
                              offer.poi_id
                      )consumer
                       on sender.campaign_id = consumer.campaign_id
                       and sender.source = consumer.source
                           and sender.stat_date = consumer.stat_date
                                      and sender.poi_id = consumer.poi_id
     )tmp
  JOIN (
         select outer_campaign_id,
           campaign_id,
           tenant_id,
           source,
           partition_date
         FROM mart_crm.dwd_crm_campaign_mapping
         WHERE
           partition_date = '2018-01-08'
       )mapping
    on  tmp.campaign_id = mapping.outer_campaign_id --23379094
        and tmp.source  = mapping.source
  JOIN (
         SELECT tenant_id AS tenant_id,
                id AS campaign_id,
                to_date(start_time) as campaign_start_date,
           campaign_name,
                case when status in (0) and end_time < '$now.delta(-1).date'   then 4 -- EXPIRED
                when status in (0) and start_time < '$now.delta(-1).date' then 1 -- UNDERWAY
                else status end as campaign_status,
                type as campaign_type,
                restrict_type as campaign_restrict_type
         FROM mart_crm.dim_crm_campaign_chain
         WHERE
           dp = 'ACTIVE'
           AND id not in (1100000000001)-- 无效活动
       )campaign
    on mapping.campaign_id = campaign.campaign_id
)t