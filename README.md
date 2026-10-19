# CS-340

repository for CS 340 class with Professor Kellogg

**How do you write programs that are maintainable, readable, and adaptable?**

When writing programs, I try to focus on keeping my code organized, understandable, and reusable. One of the biggest examples of this in CS 340 was developing the CRUD Python module in Project One and then reusing it in Project Two. Instead of writing a new database connection and separate operations for the dashboard, I was able to import my existing `AnimalShelter` class and use its `read()` method to retrieve information from MongoDB.

This approach made the dashboard easier to develop because the database operations were already separated from the user interface. It also means that if I need to change how the application communicates with the database, I can make those changes in the CRUD module rather than throughout the dashboard. In the future, I could reuse or adapt this module for other applications that need to store, retrieve, update, or delete records.

**How do you approach a problem as a computer scientist?**

I approach problems by first trying to understand what is being requested and then breaking the requirements into smaller, manageable tasks. For the Grazioso Salvare project, I started by reviewing the specifications to understand what information the organization needed and how it should be presented. From there, I developed MongoDB queries using the required breeds, sex, and age ranges before connecting them to the dashboard's interactive components.

This project was different from many of my previous assignments because I was not just writing code to demonstrate a particular programming concept. I was combining a database, a reusable Python module, and an interactive dashboard to meet a client's requirements. I also had to consider how someone else would interact with the finished application. Testing each component individually helped me identify problems without having to troubleshoot the entire project at once.

In future projects, I would continue using this approach by reviewing client requirements, planning the database structure, separating functionality into reusable components, and testing throughout development rather than waiting until the end.

**What do computer scientists do, and why does it matter?**

I believe computer scientists do more than write code. They analyze problems, develop solutions, and create systems that help people accomplish tasks more efficiently. This can involve designing databases, developing software, improving existing systems, or finding better ways to organize and use information.

The Grazioso Salvare project demonstrated how software can support an organization's work. Without the dashboard, identifying dogs that meet specific rescue training requirements could involve manually searching through thousands of animal records. By using MongoDB queries and an interactive dashboard, the organization can narrow those records based on its preferred criteria and review the results through a data table, breed distribution chart, and geolocation map.

Projects like this have helped me better understand how the different areas of computer science work together. The value of a program is not just whether the code runs correctly, but whether the finished application addresses the problem it was designed to solve.
