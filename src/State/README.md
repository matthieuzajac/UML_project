# State Transition Diagrams - Documentation

## Overview

The improved state transition diagrams provide comprehensive visualizations of all major entity lifecycles in the Royal Road Clone webnovel platform.

## What's New and Improved

### Visual Enhancements
- **Color-coded states**: Each state type uses distinct background and border colors for instant recognition
  - 🟦 Blue: Draft/Pending states
  - 🟩 Green: Active states
  - 🟨 Yellow/Orange: Hiatus/Paused states
  - 🟦 Cyan: Completed states
  - ⬜ Gray: Shadowbanned/Moderated states
  - 🟥 Red: Deleted states
  - 🟪 Purple: Pending/Under review states

- **Better organization**: States grouped into logical packages with clear borders
- **Enhanced descriptions**: Each state includes detailed notes about its purpose and behavior
- **Transition details**: All transitions show triggering events, conditions, and actions

### Content Improvements

#### 1. Novel Lifecycle (Enhanced)
- Added entry/exit actions for each state
- Included self-transitions for in-state operations
- More detailed transition conditions
- Clear moderator action flows
- Grace period information for deletions

#### 2. Chapter Lifecycle (New)
- Complete lifecycle from draft to archive/delete
- Anti-spam validation states
- Version tracking for published chapters
- Proper cleanup and archival flows

#### 3. Review Lifecycle (New)
- Draft writing state with auto-save
- Pending validation with guideline checks
- Published state with helpful votes tracking
- Hidden state for moderated content
- Complete moderation workflow

#### 4. Report Lifecycle (New)
- Creation and queuing process
- Moderator assignment and investigation
- Resolution with actions taken
- Dismissal with reason logging
- Priority assignment and evidence gathering

#### 5. Subscription Lifecycle (New)
- Active state with notifications
- Paused state without notifications
- Unsubscribe with history preservation
- Re-subscription capability

#### 6. Library Entry Lifecycle (New)
- Plan to read state with priorities
- Active reading with progress tracking
- On hold state for paused reading
- Completed state with recommendations
- Dropped state with stats preservation
- Removed state with history archiving
- Full state transition matrix (15+ transitions)

## State Notation

Each state includes:
- **Description**: What the state represents
- **Entry action**: What happens when entering the state
- **Do action**: Continuous activities while in the state
- **Exit action**: What happens when leaving the state

## Transition Notation

Each transition shows:
- **Trigger**: Event that causes the transition
- **Guard condition**: When applicable (in brackets)
- **Action**: What occurs during the transition
- **Actor**: Who initiates the transition (Author, Reader, Moderator, System)

## Key Features

### Novel Lifecycle
```
Draft → Active (first chapter published)
Active ↔ Hiatus (pause/resume)
Active → Completed (final chapter)
Completed → Active (side stories)
All states → Shadowbanned (moderation)
Shadowbanned → Previous state (restoration)
All states → Deleted (with grace periods)
```

### Chapter Lifecycle
```
Draft → Pending → Published
Published → Archived (novel completed)
Any state → Deleted
```

### Review Lifecycle
```
Draft → Pending → Published
Published → Hidden → Deleted (moderation)
Published → Draft (edits require re-validation)
```

### Report Lifecycle
```
Created → Under Review → Resolved/Dismissed
Under Review → Created (reassignment)
```

### Subscription Lifecycle
```
Subscribed ↔ Paused
Any state → Unsubscribed
Unsubscribed → Subscribed (re-subscribe)
```

### Library Entry Lifecycle
```
PlanToRead → Reading ↔ OnHold
Reading → Completed/Dropped
Any state → Removed
Most states can transition to Reading
```

## Usage

These diagrams serve multiple purposes:

1. **Development**: Guide implementation of state machines
2. **Testing**: Define test cases for state transitions
3. **Documentation**: Explain system behavior to stakeholders
4. **Onboarding**: Train new developers on workflows
5. **Maintenance**: Understand impact of changes to state logic

## File Location
- Source: `/src/State/States.wsd`
- This Document: `/src/State/README.md`

## Technical Details

- **Format**: PlantUML state diagram
- **Encoding**: UTF-8 (supports French accented characters)
- **Rendering**: Compatible with PlantUML 1.2022.0+
- **Size**: ~15000 characters, 6 state machine groups

## Notes

- All state machines support self-transitions for in-state operations
- Terminal states are explicitly marked with [*]
- Some states support restoration (Deleted for novels, not for chapters/reviews)
- Grace periods vary by entity and context (7 days for active novels, 30 days for completed)
- Anti-spam and content validation occur before publication
- All moderator actions are logged with reasons
