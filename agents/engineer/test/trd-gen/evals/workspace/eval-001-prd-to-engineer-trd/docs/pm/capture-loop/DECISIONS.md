# Capture Loop Product Decisions

Status: Confirmed

- 用户提交后立即显示 pending，不等待后台处理完成。
- 同一客户端事件 ID 只产生一个处理结果。
- 三次可重试失败后显示 failed，并允许用户显式重试。
- 产品范围不要求静默无限重试。
- 当前没有未决的产品问题阻塞 Engineer TRD。
