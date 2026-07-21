export async function sendUserEvent(user, request, order, clients) {
  await clients.analytics.track({
    userId: user.id,
    email: user.email,
    ipAddress: request.ip,
    pageUrl: request.body.pageUrl
  });

  await clients.advertising.addToAudience({
    email: user.email,
    lastPurchaseAmount: order.total
  });

  await clients.payments.updateCustomer(user.paymentCustomerId, {
    email: user.email,
    metadata: { internalUserId: user.id }
  });
}
