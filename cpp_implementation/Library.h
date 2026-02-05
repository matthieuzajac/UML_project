#ifndef LIBRARY_H
#define LIBRARY_H

#include "Enums.h"
#include <string>

class Library {
private:
    int reader_id;
    int novel_id;
    int last_read_chapter;
    std::string added_at;
    ReadingStatus reading_status;

public:
    Library(int reader_id, int novel_id, int last_read_chapter,
            const std::string& added_at, ReadingStatus reading_status);
    ~Library();

    void updateProgress(int chapterNumber);
    void remove(int novelId);
};

#endif
