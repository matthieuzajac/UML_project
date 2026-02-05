#include "Authenticated_user.h"
#include "Reader.h"
#include "Author.h"
#include "Moderator.h"
#include "Novel.h"
#include "Chapter.h"
#include "Review.h"
#include "Notification.h"
#include "Library.h"
#include "Subscription.h"
#include "Genre.h"
#include "Tag.h"
#include "Report.h"
#include "Enums.h"
#include <iostream>

int main() {
    // Instantiate Reader objects
    Reader reader1(1, "john_doe", "john@example.com", "hash123", "2024-01-15", 100);
    Reader reader2(2, "jane_smith", "jane@example.com", "hash456", "2024-02-20", 250);

    // Instantiate Author objects (inherit from Reader)
    Author author1(3, "fantasy_writer", "writer1@example.com", "hash789", "2024-01-10",
                   500, 15000, "A passionate fantasy writer");
    Author author2(4, "sci_fi_author", "writer2@example.com", "hashabc", "2024-03-05",
                   300, 8000, "Science fiction enthusiast");

    // Instantiate Moderator objects (inherit from Authenticated_user)
    Moderator moderator1(5, "admin_mod", "admin@platform.com", "hashdef", "2024-01-01", 3);
    Moderator moderator2(6, "content_mod", "content@platform.com", "hashghi", "2024-02-15", 2);

    // Instantiate Novel objects
    Novel novel1(101, "The Dragon's Quest", "An epic fantasy adventure",
                 "https://covers.example.com/dragon.jpg", 4.5f, 25000L, 50,
                 NovelStatus::ACTIVE, "2024-01-20", "2024-05-10");
    Novel novel2(102, "Stars Beyond", "A journey to the edge of the universe",
                 "https://covers.example.com/stars.jpg", 4.2f, 18000L, 35,
                 NovelStatus::ACTIVE, "2024-02-25", "2024-05-08");
    Novel novel3(103, "Shadow Chronicles", "Draft novel", "", 0.0f, 0L, 0,
                 NovelStatus::DRAFT, "2024-05-01", "2024-05-01");

    // Instantiate Chapter objects
    Chapter chapter1(1001, 1, "The Beginning", "Once upon a time...", 2500, 5000L,
                     "2024-01-25", false);
    Chapter chapter2(1002, 2, "The Journey Continues", "And so they set forth...", 3000, 4500L,
                     "2024-02-01", false);
    Chapter chapter3(1003, 1, "First Contact", "The ship landed on the alien world...", 2800, 3000L,
                     "2024-03-01", true);

    // Instantiate Review objects
    Review review1(2001, 101, 1, "Amazing story! Can't wait for more!", 5, "2024-04-10", 25);
    Review review2(2002, 102, 2, "Great world building but slow pacing", 4, "2024-04-15", 12);
    Review review3(2003, 101, 2, "One of my favorites!", 5, "2024-04-20", 30);

    // Instantiate Notification objects
    Notification notification1(3001, 1, "New chapter published for The Dragon's Quest!",
                               NotificationType::NEW_CHAPTER, false, "2024-05-10");
    Notification notification2(3002, 2, "Your review was marked helpful",
                               NotificationType::NEW_REVIEW, true, "2024-04-16");
    Notification notification3(3003, 3, "Your novel has been published",
                               NotificationType::SYSTEM_MESSAGE, true, "2024-01-25");

    // Instantiate Library objects
    Library library1(1, 101, 5, "2024-04-01", ReadingStatus::READING);
    Library library2(2, 102, 3, "2024-03-20", ReadingStatus::COMPLETED);
    Library library3(1, 102, 10, "2024-05-05", ReadingStatus::PLAN_TO_READ);

    // Instantiate Subscription objects
    Subscription subscription1(1, 101, "2024-04-01", true);
    Subscription subscription2(2, 102, "2024-03-20", true);
    Subscription subscription3(1, 102, "2024-05-05", false);

    // Instantiate Genre objects
    Genre genre1(1, "Fantasy", "Magical worlds and creatures");
    Genre genre2(2, "Science Fiction", "Futuristic settings and technology");
    Genre genre3(3, "Romance", "Love stories and relationships");

    // Instantiate Tag objects
    Tag tag1(1, "action");
    Tag tag2(2, "adventure");
    Tag tag3(3, "magic");
    Tag tag4(4, "space");
    Tag tag5(5, "dragons");

    // Instantiate Report objects
    Report report1(5001, 1, "Review", 2001, "Inappropriate language", ReportStatus::PENDING, "2024-05-12");
    Report report2(5002, 2, "Novel", 102, "Copyright violation", ReportStatus::REVIEWED, "2024-05-11");
    Report report3(5003, 1, "Chapter", 1002, "Spam content", ReportStatus::RESOLVED, "2024-05-10");

    std::cout << "All objects instantiated successfully!" << std::endl;
    return 0;
}
