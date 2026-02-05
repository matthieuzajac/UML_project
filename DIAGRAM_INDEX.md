# UML Diagram Index

Quick reference guide to all diagrams in this repository.

## 📊 Structural Diagrams (Static Structure)

### 1. Class Diagram
**File**: `src/Class.wsd`  
**Purpose**: Complete domain model with all entities, attributes, methods, and relationships  
**Key Elements**:
- Abstract class: `Authenticated_user`
- Concrete classes: `Reader`, `Author`, `Moderator`, `Novel`, `Chapter`, `Review`, `Notification`, `Library`, `Subscription`, `Genre`, `Tag`, `Report`
- 4 Enums: `NovelStatus`, `NotificationType`, `ReadingStatus`, `ReportStatus`
- Relationships: Inheritance, Composition, Aggregation, Association

**View this to understand**: The complete data model and object structure

---

### 2. Component Diagram
**File**: `src/Component.wsd`  
**Purpose**: System architecture showing services, layers, and dependencies  
**Key Layers**:
- Frontend Layer (Web UI, Mobile App)
- API Gateway (REST API, WebSocket)
- Application Services (9 services)
- Core Business Logic (6 modules)
- Infrastructure Services (5 services)
- Databases (Primary, Cache, Search Index)

**View this to understand**: How the system is organized into services

---

### 3. Package Diagram
**File**: `src/Package.wsd`  
**Purpose**: Logical organization of code into packages  
**Key Packages**:
- Presentation Layer (Web, Mobile, API Controllers)
- Business Logic Layer (5 domain packages)
- Service Layer (Core, Feature, Support services)
- Data Access Layer (Repositories, Mappers)
- Infrastructure Layer (External services, Database)

**View this to understand**: Code organization and layered architecture

---

### 4. Deployment Diagram
**File**: `src/Deployment.wsd`  
**Purpose**: Physical infrastructure and deployment topology  
**Key Nodes**:
- Client Devices (Browsers, Mobile)
- CDN (Static assets, Images)
- Load Balancer (Nginx)
- Web/App Server Clusters
- Database Cluster (Master-Slave)
- Cache Layer (Redis)
- Search Infrastructure (Elasticsearch)
- Object Storage (S3/MinIO)
- Background Workers
- External Services (Email, Monitoring, Logging)

**View this to understand**: How the system is deployed in production

---

### 5. Object Diagram
**File**: `src/Object.wsd`  
**Purpose**: Concrete runtime example with actual instance data  
**Example Scenario**: Reader "john_reader" subscribed to novel "Chronicles of the Azure Realm" by author "jane_writer", tracking reading progress, reviews, and notifications

**View this to understand**: What actual data looks like at runtime

---

## 🎭 Behavioral Diagrams (Dynamic Behavior)

### 6. Use Case Diagram
**File**: `src/Use_case.wsd`  
**Purpose**: All system capabilities and actor interactions  
**Actors**: Guest (4 use cases), Authenticated_User (6 use cases), Reader (5 use cases), Author (5 use cases), Moderator (5 use cases)  
**Total Use Cases**: 23

**View this to understand**: What users can do in the system

---

### 7. State Diagram
**File**: `src/States.wsd`  
**Purpose**: Novel entity lifecycle and state transitions  
**States**: Draft → Active → Hiatus → Completed, with Shadowbanned and Deleted states  
**Transitions**: Publication, status updates, moderation actions

**View this to understand**: How a novel's status changes over time

---

### 8. Timing Diagram
**File**: `src/Timing.wsd`  
**Purpose**: Real-time behavior during chapter publication  
**Timeline**: Author publishes → Validation → DB save → Notification creation → WebSocket broadcast → Email delivery  
**Duration**: ~500ms for complete flow

**View this to understand**: Real-time notification delivery timing

---

## 🔄 Activity Diagrams (Workflows)

### 9. Reading Workflow
**File**: `src/Activity/reading.wsd`  
**Flow**: Search → Browse → Read chapters → Progress tracking → Library/Subscribe → Review  
**Actors**: Guest, Reader

**View this to understand**: Reader journey from discovery to engagement

---

### 10. Content Submission Workflow
**File**: `src/Activity/soumission.wsd`  
**Flow**: Draft → Publish → Validation (anti-spam) → Optional moderation → Publish → Notify  
**Actors**: Author, Moderator (optional)

**View this to understand**: How content gets published and validated

---

### 11. Search Workflow
**File**: `src/Activity/search.wsd`  
**Flow**: Set criteria (keywords, genres, tags, filters) → Search → Sort → Browse → Select  
**Filters**: Status, rating, genres, tags  
**Sort Options**: Popularity, rating, date, updates, chapters

**View this to understand**: How readers discover novels

---

### 12. Author Workflow
**File**: `src/Activity/author_workflow.wsd`  
**Flow**: Create novel → Add metadata → Write chapters → Publish → Analytics → Manage status  
**Covers**: Complete author journey from creation to management

**View this to understand**: Author's complete workflow

---

## 📨 Sequence Diagrams (Interactions)

### 13. Authentication
**File**: `src/Sequence/authentication.wsd`  
**Scenarios**: Login flow, Registration flow  
**Participants**: User, UI, AuthService, Database

**View this to understand**: How users log in and register

---

### 14. Chapter Publication
**File**: `src/Sequence/chapter_publish.wsd`  
**Flow**: Author publishes → Create chapter → Save → Update rating → Notify followers  
**Participants**: Author, UI, Novel, Chapter, NotificationService, Database

**View this to understand**: What happens when a chapter is published

---

### 15. Library Management
**File**: `src/Sequence/library.wsd`  
**Flow**: Reader adds novel → Check duplicate → Get details → Save relation  
**Participants**: Reader, UI, Library, Novel, Database

**View this to understand**: How library management works

---

### 16. Subscription Management
**File**: `src/Sequence/subscription.wsd`  
**Scenarios**: Subscribe, Unsubscribe, New chapter notification delivery  
**Participants**: Reader, Author, UI, Subscription, Novel, NotificationService, Database

**View this to understand**: How subscriptions and notifications work

---

### 17. Review Submission
**File**: `src/Sequence/reviewing.wsd`  
**Flow**: Submit review → Create → Save → Update novel rating  
**Participants**: Reader, UI, Review, Novel, Database

**View this to understand**: How reviews are submitted and processed

---

### 18. Content Moderation
**File**: `src/Sequence/moderation.wsd`  
**Flow**: View reports → Take action (shadowban) → Notify author  
**Participants**: Moderator, UI, Novel, Author, NotificationService

**View this to understand**: How moderators handle content issues

---

### 19. Content Reporting
**File**: `src/Sequence/report_content.wsd`  
**Scenarios**: Submit report, Moderator review (resolve or dismiss)  
**Participants**: User, Moderator, UI, Report, NotificationService, Database

**View this to understand**: Complete reporting and moderation workflow

---

## 📋 Navigation by Purpose

### I want to understand the data model
→ Start with: **Class Diagram** (`src/Class.wsd`)  
→ See example: **Object Diagram** (`src/Object.wsd`)

### I want to understand system architecture
→ Start with: **Component Diagram** (`src/Component.wsd`)  
→ Then see: **Package Diagram** (`src/Package.wsd`)  
→ For deployment: **Deployment Diagram** (`src/Deployment.wsd`)

### I want to understand what users can do
→ Start with: **Use Case Diagram** (`src/Use_case.wsd`)  
→ Then explore relevant Activity and Sequence diagrams

### I want to understand user workflows
→ **Reader**: Activity/reading.wsd, Activity/search.wsd  
→ **Author**: Activity/author_workflow.wsd, Activity/soumission.wsd  
→ **All users**: Sequence/authentication.wsd

### I want to understand specific features

| Feature | Activity Diagram | Sequence Diagram |
|---------|-----------------|------------------|
| Reading novels | Activity/reading.wsd | - |
| Publishing chapters | Activity/author_workflow.wsd, Activity/soumission.wsd | Sequence/chapter_publish.wsd |
| Reviews & Ratings | Activity/reading.wsd | Sequence/reviewing.wsd |
| Library management | Activity/reading.wsd | Sequence/library.wsd |
| Subscriptions | Activity/reading.wsd | Sequence/subscription.wsd |
| Search & Discovery | Activity/search.wsd | - |
| Authentication | - | Sequence/authentication.wsd |
| Moderation | - | Sequence/moderation.wsd, Sequence/report_content.wsd |

### I want to understand state changes
→ **Novel states**: States.wsd  
→ **Real-time behavior**: Timing.wsd

---

## 🔍 Quick Reference by Actor

### Guest
- **Use Cases**: UC1, UC2, UC14, UC15 (Use_case.wsd)
- **Workflows**: Activity/reading.wsd, Activity/search.wsd

### Reader
- **Use Cases**: UC5, UC6, UC7, UC17, UC18 (Use_case.wsd)
- **Workflows**: Activity/reading.wsd, Activity/search.wsd
- **Interactions**: Sequence/library.wsd, Sequence/reviewing.wsd, Sequence/subscription.wsd, Sequence/report_content.wsd

### Author
- **Use Cases**: UC8, UC9, UC10, UC19, UC20 (Use_case.wsd)
- **Workflows**: Activity/author_workflow.wsd, Activity/soumission.wsd
- **Interactions**: Sequence/chapter_publish.wsd, Sequence/subscription.wsd

### Moderator
- **Use Cases**: UC11, UC12, UC21, UC22, UC23 (Use_case.wsd)
- **Workflows**: None (moderation is reactive)
- **Interactions**: Sequence/moderation.wsd, Sequence/report_content.wsd

---

## 📈 Diagram Statistics

| Category | Count | Completeness |
|----------|-------|--------------|
| **Structural Diagrams** | 5 | ✅ Complete |
| **Behavioral - Use Case** | 1 | ✅ Complete |
| **Behavioral - State** | 1 | ✅ Complete |
| **Behavioral - Activity** | 4 | ✅ Complete |
| **Behavioral - Sequence** | 7 | ✅ Complete |
| **Behavioral - Timing** | 1 | ✅ Complete |
| **Total Diagrams** | **19** | **100%** |

---

## 🎯 Recommended Learning Path

### For Developers
1. **Class.wsd** - Understand the domain model
2. **Component.wsd** - See the architecture
3. **Package.wsd** - Understand code organization
4. **Sequence/** - Study specific feature implementations
5. **Deployment.wsd** - Learn the infrastructure

### For Product Managers
1. **Use_case.wsd** - All system capabilities
2. **Activity/reading.wsd** - User journey
3. **Activity/author_workflow.wsd** - Author experience
4. **States.wsd** - Content lifecycle

### For QA/Testers
1. **Use_case.wsd** - Test scenarios
2. **Sequence/** - Interaction flows to test
3. **Activity/** - End-to-end workflows
4. **States.wsd** - State transition testing

### For DevOps/SRE
1. **Deployment.wsd** - Infrastructure setup
2. **Component.wsd** - Service dependencies
3. **Timing.wsd** - Performance expectations

### For System Architects
1. **Component.wsd** - Service architecture
2. **Package.wsd** - Logical organization
3. **Deployment.wsd** - Physical architecture
4. **Class.wsd** - Data model
5. **Sequence/** - Integration patterns

---

## 🔗 Related Documents

- **README.md** - Complete project documentation
- **COHERENCE_VALIDATION.md** - Validation report proving all diagrams are coherent
- **.gitignore** - PlantUML project gitignore

---

**Last Updated**: 2024-02-05  
**Total Diagrams**: 19  
**Status**: ✅ Complete and Coherent
