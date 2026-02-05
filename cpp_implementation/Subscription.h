#ifndef SUBSCRIPTION_H
#define SUBSCRIPTION_H

#include <string>

class Subscription {
private:
    int reader_id;
    int novel_id;
    std::string subscribed_at;
    bool notify_on_update;

public:
    Subscription(int reader_id, int novel_id, const std::string& subscribed_at,
                  bool notify_on_update);
    ~Subscription();

    void unsubscribe();
};

#endif
