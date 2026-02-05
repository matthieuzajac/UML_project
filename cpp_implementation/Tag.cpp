#include "Tag.h"
#include "Novel.h"

Tag::Tag(int id, const std::string& name)
    : id(id), name(name) {}

Tag::~Tag() {
}

std::vector<Novel*> Tag::getNovels() {
    return std::vector<Novel*>();
}
