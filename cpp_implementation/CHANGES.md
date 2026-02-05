# Changes Summary

## 1. State Diagram Improvements

Fixed the state diagram (`src/State/States.wsd`) to reduce overlapping links:

### Changes Made:
- Simplified transition labels to reduce text length
- Added `skinparam maxMessageSize 150` for better text wrapping
- Used directional hints (`-down->`, `-left->`, `-up->`) for restoration transitions from Shadowbanned
- Grouped related transitions with clear comments
- Consolidated multiple deletion transitions into fewer lines
- Reduced redundant text in state descriptions

### Visual Improvements:
- Cleaner transition paths with less crossing
- More organized layout with grouped transitions
- Better readability with shorter labels
- Clearer separation between internal transitions, main transitions, moderation actions, and deletions

## 2. C++ Implementation

Created a complete, compilable C++ implementation in `cpp_implementation/` folder.

### Files Created:

#### Header Files (14):
1. `Enums.h` - All enumeration types (NovelStatus, NotificationType, ReadingStatus, ReportStatus)
2. `Authenticated_user.h` - Abstract base class
3. `Reader.h` - Reader class
4. `Author.h` - Author class (inherits from Reader)
5. `Moderator.h` - Moderator class
6. `Novel.h` - Novel entity
7. `Chapter.h` - Chapter entity
8. `Review.h` - Review entity
9. `Notification.h` - Notification entity
10. `Library.h` - Library management
11. `Subscription.h` - Subscription management
12. `Genre.h` - Genre entity
13. `Tag.h` - Tag entity
14. `Report.h` - Report entity

#### Implementation Files (14):
Corresponding `.cpp` files for each header containing method definitions with empty implementations.

#### Main Program (1):
- `main.cpp` - Instantiates all 27 objects modeled in the class diagram:
  - 2 Reader objects
  - 2 Author objects
  - 2 Moderator objects
  - 3 Novel objects (one in DRAFT, two in ACTIVE status)
  - 3 Chapter objects
  - 3 Review objects
  - 3 Notification objects
  - 3 Library objects
  - 3 Subscription objects
  - 3 Genre objects
  - 5 Tag objects
  - 3 Report objects

#### Documentation (1):
- `README.md` - Complete documentation of the C++ implementation

### Compilation:
```bash
cd cpp_implementation
g++ -std=c++17 -o program *.cpp
./program
```

Successfully tested and verified to compile without errors.

### Class Hierarchy Implemented:
```
Authenticated_user (abstract)
├── Reader
│   └── Author
└── Moderator
```

### Key Relationships Implemented:
- **Inheritance**: Author → Reader → Authenticated_user; Moderator → Authenticated_user
- **Composition**: Novel owns Chapters (handled through Novel destructor)
- **Aggregation**: Readers and Novels associated with Reviews
- **Associations**: Users with entities they create or manage
