import java.time.LocalDateTime
import java.time.format.DateTimeFormatter.ofPattern
import scala.Option.empty
import scala.concurrent.duration.{Duration,MINUTES}
import scala.io.StdIn.{readInt,readLine}

object CalendarCLI {
  var calendar: List[(String, LocalDateTime, Duration)] = List()

  def displayMenu(): Unit = {
    println("1. View Calendar")
    println("2. Add entry")
    println("3. Modify entry")
    println("4. Delete entry")
    println(">")
  }

  def displayCalendar(): Unit = {
    println("---------")
    calendar.zipWithIndex.foreach {
      case (e, i) => println(i + ". " + e._2 + " - " + e._1 + " - " + e._3)
    }
    println("---------")
  }

  def deleteEntry(entryId: Int): Unit = {
    calendar = calendar.patch(entryId, Nil, 1)
  }

  def createEntry(name: Option[String], start: Option[LocalDateTime], duration: Option[Duration]): Unit = {
    println("Enter the name of the entry" + name.map(n => f"(Press enter to keep $n)").getOrElse(""))
    print(">")

    val entryNameInput: String = readLine()
    val entryName = if (entryNameInput.length == 0) name.get else entryNameInput

    println("Enter the starting date of the entry YYYY-MM-DD HH:mm" + start.map(d => s"(Press enter to keep $d").getOrElse(""))
    print(">")
    val entryStartInput: String = readLine()
    val entryStart = if (entryStartInput.length == 0) start.get else LocalDateTime.parse(entryStartInput, ofPattern("yyyy-MM-dd HH:mm"))

    println("Enter the duration of the entry in minutes" + duration.map(d => s"(Press enter to keep $d").getOrElse(""))
    val entryDurationInput: String = readLine()
    val entreDuration = if (entryDurationInput == 0) duration.get else Duration(entryDurationInput.toInt, MINUTES)
    calendar = calendar.appended((entryName, entryStart, entreDuration))
  }

  def processInput(userInput: Int): Unit = {
    if (userInput == 1) {
      displayCalendar()
    } else if (userInput == 2) {
      createEntry(empty, empty, empty)
    } else if (userInput == 3) {
      displayCalendar()
      println("What calendar entry do you to modify")
      print(">")
      val entryId = readInt()
      val entry = calendar(entryId)
      deleteEntry(entryId)
      createEntry(Option(entry._1), Option(entry._2), Option(entry._3))
    } else if (userInput == 4) {
      displayCalendar()
      println("What calendar entry do you want to delete")
      print(">")
      deleteEntry(readInt())
    } else if (userInput == 5) {
      System.exit(1)
    }
  }

  def main(args: Array[String]): Unit = {
    while (true) {
      displayMenu()
      val userInput = readInt()
      processInput(userInput)
    }
  }
}
