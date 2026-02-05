#ifndef TAG_H
#define TAG_H

#include <string>
#include <vector>

class Novel;

class Tag {
private:
    int id;
    std::string name;

public:
    Tag(int id, const std::string& name);
    ~Tag();

    std::vector<Novel*> getNovels();
};

#endif
