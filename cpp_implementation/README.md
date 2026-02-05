# C++ Implementation of Royal Road Clone Class Diagram

This folder contains a complete, compilable C++ implementation of the class diagram modeled in `src/Class.wsd`.

## Structure

### Header Files (.h)
- `Enums.h` - Enumeration types (NovelStatus, NotificationType, ReadingStatus, ReportStatus)
- `Authenticated_user.h` - Abstract base class for all authenticated users
- `Reader.h` - Reader class inheriting from Authenticated_user
- `Author.h` - Author class inheriting from Reader
- `Moderator.h` - Moderator class inheriting from Authenticated_user
- `Novel.h` - Novel entity class
- `Chapter.h` - Chapter entity class
- `Review.h` - Review entity class
- `Notification.h` - Notification entity class
- `Library.h` - Library management class
- `Subscription.h` - Subscription management class
- `Genre.h` - Genre entity class
- `Tag.h` - Tag entity class
- `Report.h` - Report entity class

### Implementation Files (.cpp)
- `Authenticated_user.cpp` - Method definitions for Authenticated_user
- `Reader.cpp` - Method definitions for Reader
- `Author.cpp` - Method definitions for Author
- `Moderator.cpp` - Method definitions for Moderator
- `Novel.cpp` - Method definitions for Novel
- `Chapter.cpp` - Method definitions for Chapter
- `Review.cpp` - Method definitions for Review
- `Notification.cpp` - Method definitions for Notification
- `Library.cpp` - Method definitions for Library
- `Subscription.cpp` - Method definitions for Subscription
- `Genre.cpp` - Method definitions for Genre
- `Tag.cpp` - Method definitions for Tag
- `Report.cpp` - Method definitions for Report

### Main Program
- `main.cpp` - Instantiates all objects modeled in the class diagram

## Compilation

To compile the program:

```bash
g++ -std=c++17 -o program *.cpp
```

Or compile each file separately:

```bash
g++ -std=c++17 -c *.cpp
g++ -std=c++17 -o program *.o
```

To run the program:

```bash
./program
```

## Class Hierarchy

```
Authenticated_user (abstract)
├── Reader
│   └── Author
└── Moderator
```

## Key Entities

- **Novel**: Contains multiple Chapters (composition relationship)
- **Chapter**: Part of a Novel with content and metadata
- **Review**: Written by a Reader for a Novel
- **Notification**: Sent to Authenticated_users about various events
- **Library**: Manages Reader's reading progress
- **Subscription**: Reader's subscription to Novel updates
- **Genre/Tag**: Categorization for Novels
- **Report**: Content moderation reports

## Relationships Implemented

1. **Inheritance**: Author inherits from Reader, which inherits from Authenticated_user; Moderator inherits from Authenticated_user
2. **Composition**: Novel owns Chapters (chapters are deleted when novel is deleted)
3. **Aggregation**: Readers and Novels are associated with Reviews
4. **Associations**: Various user types with entities they create or manage
