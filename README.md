# Calendarmd - Manage your schedule in plaintext
Calendarmd is an experimental new format for writing schedules and events in markdown. 
The purpose of this project is to offer an alternative to traditional iCal-based calendars
that can easily be read, edited, and synced across devices, without the need of a protocol
such as CalDav.

This repo also includes very simple python scripts to write and interpret data from calendar.md files.
As of the last commit, these include:
- A script that generates blank calendar.md files
- A script that prints a weekly schedule with the current day as start date

I am not a python developer, and have created this project simply by curiosity and necessity to have a
simple way of synchronizing events between my devices without the use of a CalDav server such as Radicale.
That being said, please feel free to suggest changes or to fork this project and take it where you will.

# Inspired by
- [Calendar.txt](https://terokarvinen.com/2021/calendar-txt/)
- [Todo.txt](https://github.com/todotxt/todo.txt)

# How to use the calendar.md format:
Please, see example.md for a full example.
- Level 1 headings contain each date in ISO format, with the ordinal date number, week number, and weekday number.
- Level 2 headings denote particular events, marked by their scheduled time followed by a ">" sign and the event name.
- Whole-day events are marked with an "x".
- Multi-day events have their first day marked with a "x-", the last day with a "-x", and all middle days with "-x-"
- Text beneath level 2 headings contain details about the event.



