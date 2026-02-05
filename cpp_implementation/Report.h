#ifndef REPORT_H
#define REPORT_H

#include "Enums.h"
#include <string>

class Report {
private:
    int id;
    int reporter_id;
    std::string content_type;
    int content_id;
    std::string reason;
    ReportStatus status;
    std::string created_at;

public:
    Report(int id, int reporter_id, const std::string& content_type, int content_id,
           const std::string& reason, ReportStatus status, const std::string& created_at);
    ~Report();

    void resolve();
};

#endif
