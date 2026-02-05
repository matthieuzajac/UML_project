#include "Library.h"

Library::Library(int reader_id, int novel_id, int last_read_chapter,
                 const std::string& added_at, ReadingStatus reading_status)
    : reader_id(reader_id), novel_id(novel_id), last_read_chapter(last_read_chapter),
      added_at(added_at), reading_status(reading_status) {}

Library::~Library() {
}

void Library::updateProgress(int chapterNumber) {
}

void Library::remove(int novelId) {
}
