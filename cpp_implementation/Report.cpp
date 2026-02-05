#include "Report.h"

Report::Report(int id, int reporter_id, const std::string& content_type, int content_id,
               const std::string& reason, ReportStatus status, const std::string& created_at)
    : id(id), reporter_id(reporter_id), content_type(content_type), content_id(content_id),
      reason(reason), status(status), created_at(created_at) {}

Report::~Report() {
}

void Report::resolve() {
}
