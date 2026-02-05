#ifndef NOTIFICATION_H
#define NOTIFICATION_H

#include "Enums.h"
#include <string>

class Notification {
private:
    int id;
    int user_id;
    std::string message;
    NotificationType type;
    bool is_read;
    std::string created_at;

public:
    Notification(int id, int user_id, const std::string& message,
                NotificationType type, bool is_read, const std::string& created_at);
    ~Notification();

    void send();
    void markAsRead();
};

#endif
