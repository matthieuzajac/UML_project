#include "Subscription.h"

Subscription::Subscription(int reader_id, int novel_id, const std::string& subscribed_at,
                            bool notify_on_update)
    : reader_id(reader_id), novel_id(novel_id), subscribed_at(subscribed_at),
      notify_on_update(notify_on_update) {}

Subscription::~Subscription() {
}

void Subscription::unsubscribe() {
}
