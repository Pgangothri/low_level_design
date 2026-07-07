C++
|
Java
|
Python
Introduction
Behavioral design patterns focus on how objects interact and communicate with each other, helping to define the flow of control in a system. These patterns simplify complex communication logic between objects while promoting loose coupling.

Imagine a TV remote that lets you switch through channels one by one, without needing to know how the channels are stored internally. This kind of controlled access is exactly what behavioral patterns help us achieve.

One such pattern is the Iterator Pattern. Let's understand the Iterator Pattern in depth in the upcoming sections.

Iterator Pattern
The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of a collection sequentially without exposing the underlying representation.
Formal Definition
The Iterator Pattern is a behavioral design pattern that entrusts the traversal behavior of a collection to a separate design object. It traverses the elements without exposing the underlying operations.

This means whether your collection is a list, a tuple, a generator, a tree, or something custom, you can use an iterator to traverse it in a consistent manner, one element at a time, without worrying about how the data is stored or managed internally.
Real-Life Analogy
Think of a vending machine. You don’t need to know how the snacks are arranged inside or where exactly your favorite drink is stored. You just press the "Next" button to scroll through options one by one. The vending machine controls the order and pace of traversal.

Similarly, an iterator acts like that "Next" button, giving you one item at a time, hiding the complexity of what’s going on behind the scenes.

Understanding the Problem
Let’s say we’re building a YouTube Playlist system. We want to store a list of videos and print their titles one by one. Let's look at the initial code setup:
Python


from typing import List

# A simple Video class with title
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title

# YouTubePlaylist class holds a list of Video objects
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def get_videos(self) -> List[Video]:
        # Expose internal list (this is the main design issue)
        return self._videos

# Client Code
def main() -> None:
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Loop through videos and print titles
    for v in playlist.get_videos():
        print(v.get_title())

if __name__ == "__main__":
    main()
What are the Issues?
While the code works, there are several design-level concerns:
Exposes internal structure:
The internal list is directly returned via get_videos() or similar methods.
This breaks encapsulation, as clients can access or even modify the internal collection outside the owning class.
Tight coupling with underlying structure:
The external code is tightly bound to the specific type of collection used (like list, deque, etc.).
Any change in the internal structure may require changes in client code.
No control over traversal
Traversal logic is managed outside the class.
You can't enforce custom traversal behaviors (e.g., reverse, skip elements, filter) without modifying external code.
Difficult to support multiple independent traversals:
If two parts of your program want to iterate over the same playlist independently, there's no built-in way to do that cleanly.
You have to manage indexing and traversal state manually.

Let us now understand how we can solve this problem using the Iterator Pattern.

The Solution
To fix the issues like exposing internal data and lacking control over traversal, we can apply the Iterator Pattern. This pattern lets external code access playlist items sequentially without knowing or modifying the internal data structure.

Let’s implement this using custom interfaces and iterator classes.
Python


from typing import List, Optional, Protocol

# ========== Video class representing a single video ==========
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title

# ========== YouTubePlaylist class (Aggregate) ==========
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def get_videos(self) -> List[Video]:
        # Expose internal list (still not ideal)
        return self._videos

# ========== Iterator interface ==========
class PlaylistIterator(Protocol):
    def has_next(self) -> bool:
        ...

    def next(self) -> Optional[Video]:
        ...

# ========== Concrete Iterator class ==========
class YouTubePlaylistIterator:
    def __init__(self, videos: List[Video]) -> None:
        # Store the reference to the list we iterate on
        self._videos = videos

        # Track current position
        self._position = 0

    def has_next(self) -> bool:
        # Check if more videos are left
        return self._position < len(self._videos)

    def next(self) -> Optional[Video]:
        # If no next element, return None
        if not self.has_next():
            return None

        # Return current element and move forward
        video = self._videos[self._position]
        self._position += 1
        return video

# ========== Main method (Client code) ==========
def main() -> None:
    # Create a playlist and add videos
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Client directly creates the iterator using internal list (not ideal)
    iterator: PlaylistIterator = YouTubePlaylistIterator(playlist.get_videos())

    # Use the iterator to loop through the playlist
    while iterator.has_next():
        video = iterator.next()
        # Defensive check in case next() returns None
        if video is not None:
            print(video.get_title())

if __name__ == "__main__":
    main()
How This Solves the Problem:
With the iterator pattern in place, we’ve clearly separated the concern of how elements are traversed from the actual data structure that stores them. Here's how this improves our design:

Problem	How Iterator Pattern Solves It
Direct access to internal data structure	The collection no longer exposes its internal data (like a list) directly for traversal. Instead, an iterator is used to access elements one-by-one, encapsulating the structure.
No standard way to iterate	All traversal is now handled through a consistent interface (has_next() / next()), regardless of how the data is stored internally. This ensures uniformity in how iteration happens.
Traversal logic spread across client code	The logic for maintaining iteration state (e.g., index or position) is encapsulated within the iterator class itself, keeping the client code clean and focused only on usage.
Difficult to customize traversal	Custom iterator classes can easily be extended to provide different traversal strategies (e.g., reverse, filtering, skipping), without changing the underlying collection.
Tight coupling to collection type	Client code no longer depends on the exact type of data structure. It interacts only with the iterator, reducing dependencies and improving flexibility.
One Major Issue Still Remains...
Even though we’ve abstracted the traversal logic into an iterator class, the client is still responsible for creating and using the iterator, which is not ideal. The goal of true encapsulation would be to hide even the creation of the iterator, something we’ll address now with a more refined approach in the next section.

More Refined Approach
This version fully aligns with the Iterator Design Pattern, where the collection itself provides the iterator, and the client is decoupled from the internal list structure.
Python


from typing import Iterator, List, Optional, Protocol

# ========== Video class representing a single video ==========
class Video:
    def __init__(self, title: str) -> None:
        # Store video title
        self._title = title

    def get_title(self) -> str:
        # Return the title
        return self._title

# ========== Iterator interface (defines traversal contract) ==========
class PlaylistIterator(Protocol):
    def has_next(self) -> bool:
        ...

    def next(self) -> Optional[Video]:
        ...

# ========== Concrete Iterator class ==========
class YouTubePlaylistIterator:
    def __init__(self, videos: List[Video]) -> None:
        # Store the list reference
        self._videos = videos

        # Track current index
        self._position = 0

    def has_next(self) -> bool:
        # Check if we still have elements
        return self._position < len(self._videos)

    def next(self) -> Optional[Video]:
        # Return None when iteration finishes
        if not self.has_next():
            return None

        # Return current item and move forward
        video = self._videos[self._position]
        self._position += 1
        return video

# ================ Playlist interface ================
# Acts as a contract for collections that are iterable
class Playlist(Protocol):
    def create_iterator(self) -> PlaylistIterator:
        ...

# ========== YouTubePlaylist class (Aggregate) ==========
# Collection provides iterator, client never sees internal list
class YouTubePlaylist:
    def __init__(self) -> None:
        # Internal list of videos
        self._videos: List[Video] = []

    def add_video(self, video: Video) -> None:
        # Add a video to playlist
        self._videos.append(video)

    def create_iterator(self) -> PlaylistIterator:
        # Each call returns a new iterator (independent traversal state)
        return YouTubePlaylistIterator(self._videos)

# ========== Main method (Client code) ==========
def main() -> None:
    # Create a playlist and add videos to it
    playlist = YouTubePlaylist()
    playlist.add_video(Video("LLD Tutorial"))
    playlist.add_video(Video("System Design Basics"))

    # Client simply asks for an iterator
    iterator = playlist.create_iterator()

    # Iterate through the playlist using the provided interface
    while iterator.has_next():
        video = iterator.next()
        # Defensive check in case next() returns None
        if video is not None:
            print(video.get_title())

if __name__ == "__main__":
    main()
Key Improvements
The YouTubePlaylist class no longer exposes its internal implementation of _videos.
The client does not manage or know about the internal structure.
The Playlist contract allows us to make other types of playlists (e.g., MusicPlaylist) that can also be iterable.
Fully aligns with the Iterator Design Pattern principles.

Ideal Scenarios for Using the Iterator Pattern
The Iterator Pattern isn’t meant for every situation, but it becomes incredibly useful in specific cases. Here are the key situations where this pattern shines:
You want to traverse a collection without exposing its internal structure:
Instead of revealing whether it's a list, deque, or a custom tree, the pattern lets clients access elements one-by-one, safely and uniformly.
You need multiple ways to traverse a collection:
For example, forward traversal, reverse traversal, or skipping every second element. Each of these can be handled by a different iterator implementation without changing the collection itself.
You want a unified way to traverse different types of collections:
Whether it’s a list of videos, a set of songs, or a stack of documents, clients should be able to iterate over them using a common interface.
You want to decouple iteration logic from collection logic:
By separating how elements are stored from how they’re accessed, you reduce complexity and improve maintainability. Changes in iteration logic won’t affect how the collection is structured, and vice versa.

Real World Examples
The Iterator Pattern is deeply embedded in software systems where data needs to be traversed without exposing its internal structure. Here are two crisp, real-world examples:
1. Python’s iter() and next() Functions
In Python, you can turn any iterable (like a list or tuple) into an iterator using iter(), and manually traverse it using next():
Python


nums = [10, 20, 30]
it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20

Under the hood, this is Python’s version of the Iterator Pattern. It works the same way across lists, sets, file streams, and even custom objects if you implement __iter__ and __next__.

2. Python for-loop
A for loop is syntactic sugar built on top of the iterator protocol. It calls iter() once, and repeatedly calls next() until StopIteration occurs:
Python


nums = [10, 20, 30]

for x in nums:
    print(x)

This is why custom iterators in Python feel natural: they plug into the same protocol used everywhere.

Important Python Details
Python has a built-in iterator protocol, so custom iterator pattern code should align with it:
StopIteration is the standard end signal:
Production-style Python iterators typically implement __next__ and raise StopIteration instead of returning None. Returning None can be ambiguous if None is a valid element.
Most Python code uses __iter__ and __next__:
If you implement these methods, your object works with for loops, comprehensions, list(), sum(), and many other built-ins automatically.
Generators are a lightweight iterator:
If traversal logic is simple, a generator function (using yield) can act as an iterator without writing a full iterator class.
Multiple independent traversals:
Returning a fresh iterator instance from create_iterator() ensures independent state, just like creating two separate iterators with iter().

Pros and Cons
Pros of Iterator Pattern
Hides internal structure:
You can traverse a collection without knowing how it's built internally.
Unified way to traverse:
You use the same methods (has_next, next) regardless of the collection type.
Supports multiple traversal strategies:
You can easily create different iterators (e.g., forward, reverse, filtered).
Follows SRP and OCP principles:
Iteration logic is separated (Single Responsibility), and new iterators can be added without modifying existing code (Open/Closed).

Cons of Iterator Pattern
Adds extra classes/interfaces:
Requires more boilerplate code to set up custom iterators.
Can be overkill for simple data structures:
For small lists, a direct for loop might be more straightforward.
External iteration is manual:
Client has to manage the loop using has_next() and next() unless abstracted further.

Class Diagram


27





Iterator Pattern - TUF+