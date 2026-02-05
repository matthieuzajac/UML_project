# Royal Road Clone - UML Documentation

This repository contains comprehensive UML diagrams for a webnovel publishing and reading platform similar to Royal Road.

## Project Overview

This is a **documentation-only** repository containing PlantUML diagrams that model the complete architecture, behavior, and structure of a webnovel platform where:
- **Authors** can publish and manage their novels
- **Readers** can discover, read, review, and follow novels
- **Moderators** can ensure content quality and enforce community guidelines
- **Guests** can browse and search for publicly available content

## Tech Stack

- **PlantUML** - UML modeling language
- `.wsd` file format for all diagrams

## Repository Structure

```
src/
├── Use_case.wsd          # Use case diagram - System capabilities and actors
├── Class.wsd             # Class diagram - Domain model and relationships
├── States.wsd            # State diagram - Novel lifecycle states
├── Component.wsd         # Component diagram - System architecture
├── Deployment.wsd        # Deployment diagram - Component distribution
├── Package.wsd           # Package diagram - Logical organization
├── Object.wsd            # Object diagram - Runtime example
├── Timing.wsd            # Timing diagram - Real-time notification flow
├── Activity/
│   ├── reading.wsd       # Reader journey workflow
│   ├── soumission.wsd    # Content submission workflow
│   ├── search.wsd        # Search and discovery workflow
│   └── author_workflow.wsd # Author complete workflow
└── Sequence/
    ├── authentication.wsd    # Login and registration flow
    ├── chapter_publish.wsd   # Chapter publication flow
    ├── library.wsd           # Add to library flow
    ├── moderation.wsd        # Content moderation flow
    ├── reviewing.wsd         # Review submission flow
    ├── subscription.wsd      # Subscribe/unsubscribe flow
    └── report_content.wsd    # Content reporting flow
```

## Diagram Descriptions

### Structural Diagrams

#### Class Diagram (`Class.wsd`)
**Purpose**: Defines the domain model with all entities, their attributes, methods, and relationships.

**Key Elements**:
- **Actors**: `Authenticated_user` (abstract), `Reader`, `Author`, `Moderator`
- **Core Entities**: `Novel`, `Chapter`, `Review`, `Notification`
- **Supporting Entities**: `Library`, `Subscription`, `Genre`, `Tag`, `Report`
- **Enums**: `NovelStatus`, `NotificationType`, `ReadingStatus`, `ReportStatus`

**Key Relationships**:
- Composition: Novel contains Chapters (lifecycle dependency)
- Aggregation: Reviews written by Readers, associated with Novels
- Association: Authors create Novels, Readers follow Novels via Subscriptions

#### Component Diagram (`Component.wsd`)
**Purpose**: Shows the system architecture with service layers and dependencies.

**Layers**:
- **Frontend Layer**: Web UI, Mobile App
- **API Gateway**: REST API, WebSocket Server
- **Application Services**: Authentication, User, Novel, Chapter, Review, Notification, Search, Moderation, Analytics
- **Core Business Logic**: User Management, Content Management, Library Management, Subscription Management, Rating System, Reporting System
- **Infrastructure Services**: Email, File Storage, Cache, Anti-Spam, Search Engine
- **Databases**: Primary DB, Cache DB, Search Index

#### Package Diagram (`Package.wsd`)
**Purpose**: Organizes the system into logical packages showing the layered architecture.

**Packages**:
- **Presentation Layer**: Web/Mobile interfaces, API controllers
- **Business Logic Layer**: Domain packages (User, Content, Engagement, Notification, Moderation, Analytics)
- **Service Layer**: Core, Feature, and Support services
- **Data Access Layer**: Repositories and data mappers
- **Infrastructure Layer**: External services, cross-cutting concerns, databases

#### Deployment Diagram (`Deployment.wsd`)
**Purpose**: Illustrates the logical deployment architecture showing how system components are distributed across different nodes.

**Architecture Layers**:
- **Client Layer**: Web browsers and mobile applications
- **Web Server**: Frontend application serving user interfaces
- **Application Server**: API Gateway, REST API, and WebSocket server
- **Business Logic Server**: Core services (User, Content, Review, Notification, Moderation, Search)
- **Data Storage**: Primary database, cache layer, and search index
- **File Storage**: Object storage for images and avatars
- **Background Workers**: Asynchronous processing for notifications, emails, and analytics

#### Object Diagram (`Object.wsd`)
**Purpose**: Shows a concrete runtime example with actual instance data.

**Example Scenario**: A reader (john_reader) who has subscribed to an active novel "Chronicles of the Azure Realm" by author jane_writer, has read up to chapter 85, left a review, and receives notifications for new chapters.

### Behavioral Diagrams

#### Use Case Diagram (`Use_case.wsd`)
**Purpose**: Defines all system use cases and actor interactions.

**Actors and Their Use Cases**:
- **Guest**: Search novels, Read public chapters, Browse by genre/tag, Register account
- **Authenticated User**: Login, Logout, Manage profile, Receive notifications, Reset password, Report content
- **Reader**: Post reviews/ratings, Manage library, Subscribe to novels, Mark reviews helpful, Track reading progress
- **Author**: Create/edit novels, Publish chapters, View analytics, Manage novel status, Add tags/genres
- **Moderator**: Delete reviews, Ban/shadowban users, Review reports, Moderate content

#### State Diagram (`States.wsd`)
**Purpose**: Models the lifecycle of a Novel entity through different states.

**States**:
- **Draft**: Initial state, invisible to readers
- **Active**: Published and visible in searches
- **Hiatus**: Paused but still visible
- **Completed**: Finished novel
- **Shadowbanned**: Hidden from public searches (moderation)
- **Deleted**: Final state, permanently removed

**Transitions**: Publishing, status updates, moderation actions, deletion

#### Timing Diagram (`Timing.wsd`)
**Purpose**: Shows real-time behavior during chapter publication and notification delivery.

**Timeline**: Demonstrates the complete flow from author clicking "Publish" through content validation, database save, notification creation, WebSocket broadcasting to online readers, and email delivery to offline readers.

### Activity Diagrams

#### Reading Workflow (`Activity/reading.wsd`)
**Purpose**: Reader journey from search to engagement.

**Flow**: Search → Browse synopsis → Read chapters → Progress tracking → Add to library/Subscribe → Leave reviews

#### Content Submission (`Activity/soumission.wsd`)
**Purpose**: Author chapter publication process.

**Flow**: Draft chapter → Publish → Validation (anti-spam) → Optional moderation review → Publish → Notify subscribers

#### Search Workflow (`Activity/search.wsd`)
**Purpose**: Novel discovery and advanced search.

**Flow**: Set search criteria (keywords, genres, tags, filters) → Execute search → Sort results → Browse → Select novel

**Search Filters**: Status, minimum rating, word count, last updated
**Sort Options**: Popularity, rating, publication date, update date, chapter count

#### Author Workflow (`Activity/author_workflow.wsd`)
**Purpose**: Complete author journey from novel creation to analytics.

**Flow**: Create novel → Add metadata (cover, genres, tags) → Write chapters → Publish → Monitor analytics → Manage status

### Sequence Diagrams

#### Authentication (`Sequence/authentication.wsd`)
**Purpose**: User login and registration flows.

**Scenarios**:
- Login: Credential validation, session creation, user data loading
- Registration: Email uniqueness check, password hashing, verification email

#### Chapter Publication (`Sequence/chapter_publish.wsd`)
**Purpose**: Interaction flow when author publishes a new chapter.

**Participants**: Author, UI, Novel, Chapter, NotificationService, Database

**Flow**: Create chapter → Save to DB → Update novel rating → Notify followers

#### Library Management (`Sequence/library.wsd`)
**Purpose**: Adding a novel to reader's library.

**Flow**: Check duplicate → Get novel details → Save relation → Confirm

#### Subscription Management (`Sequence/subscription.wsd`)
**Purpose**: Subscribe/unsubscribe to novels and notification delivery.

**Scenarios**:
- Subscribe: Create subscription → Update follower count
- New Chapter: Get subscribers → Create notifications → Send emails
- Unsubscribe: Remove subscription → Update follower count

#### Review Submission (`Sequence/reviewing.wsd`)
**Purpose**: Posting and managing reviews.

**Flow**: Create review → Save to DB → Update novel's average rating → Display

#### Moderation (`Sequence/moderation.wsd`)
**Purpose**: Content moderation actions.

**Flow**: View flagged content → Take action (shadowban/approve) → Update status → Notify author

#### Content Reporting (`Sequence/report_content.wsd`)
**Purpose**: User-generated content reports and moderator review.

**Scenarios**:
- Submit Report: Create report → Notify moderators
- Review Report: Moderator evaluates → Take action or dismiss → Notify involved parties

## Key Features Modeled

### Core Functionality
- ✅ User authentication and authorization (roles: Guest, Reader, Author, Moderator)
- ✅ Novel creation, editing, and management
- ✅ Chapter writing and publication
- ✅ Reading progress tracking
- ✅ Search and discovery (full-text, filters, sorting)
- ✅ Reviews and ratings system
- ✅ Library management (reading lists)
- ✅ Subscription and notification system

### Advanced Features
- ✅ Genre and tag categorization
- ✅ Real-time notifications (WebSocket)
- ✅ Email notifications
- ✅ Content moderation
- ✅ User reporting system
- ✅ Ban and shadowban mechanisms
- ✅ Author analytics and statistics
- ✅ Anti-spam filtering
- ✅ Premium content support (chapter-level)
- ✅ Novel status management (Draft, Active, Hiatus, Completed)

### Technical Features
- ✅ Scalable microservices architecture
- ✅ Master-slave database replication
- ✅ Redis caching layer
- ✅ Elasticsearch for search
- ✅ CDN for static assets
- ✅ Load balancing
- ✅ Asynchronous job processing
- ✅ Object storage for files

## Design Principles

### Coherence Between Diagrams
All diagrams are **cross-referenced and consistent**:
- Entities in Class diagram appear in Sequence/Activity diagrams
- Use cases map to Activity/Sequence workflows
- States from State diagram appear in Class diagram (NovelStatus enum)
- Components align with Package organization
- Deployment matches Component services

### Domain-Driven Design
- Clear separation of concerns (User, Content, Engagement, Moderation domains)
- Rich domain models with behavior (not anemic models)
- Aggregate roots (Novel aggregates Chapters)

### SOLID Principles
- **Single Responsibility**: Each service has one clear purpose
- **Open/Closed**: Extensible through interfaces (NotificationType enum)
- **Liskov Substitution**: Reader, Author, Moderator all substitute Authenticated_user
- **Interface Segregation**: Specialized services (SearchService, AnalyticsService)
- **Dependency Inversion**: Services depend on abstractions, not implementations

## How to View the Diagrams

### Online Viewers
1. **PlantUML Online**: https://www.plantuml.com/plantuml/uml/
2. **PlantText**: https://www.planttext.com/

### Local Tools
1. **Visual Studio Code**: Install "PlantUML" extension
2. **IntelliJ IDEA**: Built-in PlantUML support
3. **Command Line**:
   ```bash
   plantuml src/**/*.wsd
   ```

### Generate All Diagrams
```bash
# Install PlantUML
brew install plantuml  # macOS
apt-get install plantuml  # Ubuntu/Debian

# Generate all diagrams as PNG
find src -name "*.wsd" -exec plantuml {} \;

# Generate as SVG
find src -name "*.wsd" -exec plantuml -tsvg {} \;
```

## Actors and Permissions

| Actor | Inherits From | Key Permissions |
|-------|---------------|-----------------|
| **Guest** | - | Search, read public content, browse |
| **Authenticated_user** | - | Login, manage profile, receive notifications |
| **Reader** | Authenticated_user | Review, rate, manage library, subscribe |
| **Author** | Authenticated_user | Create novels, publish chapters, view analytics |
| **Moderator** | Authenticated_user | Delete reviews, ban users, moderate content |

## Entity Relationships Summary

```
Author (1) ----creates----> (0..*) Novel
Novel (1) ----contains----> (1..*) Chapter [Composition]
Reader (1) ----writes----> (0..*) Review
Novel (1) ----receives----> (0..*) Review [Aggregation]
Reader (1) ----manages----> (0..*) Library
Reader (1) ----has----> (0..*) Subscription
Novel (0..*) ----belongs_to----> (1..*) Genre
Novel (0..*) ----tagged_with----> (0..*) Tag
Authenticated_user (1) ----receives----> (0..*) Notification
Authenticated_user (1) ----creates----> (0..*) Report
Moderator (0..1) ----handles----> (0..*) Report
```

## State Transitions

```
[*] --> Draft
Draft --> Active (publishFirstChapter)
Active --> Hiatus (markAsHiatus)
Hiatus --> Active (publishChapter)
Active --> Completed (markAsCompleted)
Completed --> Active (addSideStory)
Active --> Shadowbanned (moderatorAction)
Shadowbanned --> Active (moderatorReview)
Shadowbanned --> Deleted (moderatorAction)
Draft --> Deleted (deleteByAuthor)
Deleted --> [*]
```

## Future Enhancements (Not Currently Modeled)

- Payment/monetization system
- Comment system for chapters
- Private messaging between users
- Author collaborations
- Translation management
- Mobile push notifications
- Advanced recommendation engine
- User achievements/badges
- Writing contests
- Author forums

## Contributing

Since this is a documentation-only repository, contributions should focus on:
- Improving diagram clarity
- Adding missing use cases or scenarios
- Fixing inconsistencies between diagrams
- Adding more detailed sequence diagrams for complex flows
- Documenting design decisions

## License

This UML documentation is provided as-is for educational and planning purposes.

## Notes

- All timestamps use ISO 8601 format
- Database IDs are integers (auto-increment)
- Passwords are hashed (never stored in plain text)
- Foreign keys maintain referential integrity
- Soft deletes are used where appropriate (can be extended)
- The system supports horizontal scaling at all layers
