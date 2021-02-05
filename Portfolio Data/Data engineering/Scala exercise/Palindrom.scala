import scala.io.StdIn.readLine;
object Palindrom {
  def reverseString(input: String):String = {
    var reversedStr = ""
    for (idx <- 0 until input.length) {
      var currentChar = input(idx)
      reversedStr = s"$currentChar$reversedStr"
    }
    reversedStr
  }
  def isPalindrom(input:String): Boolean = {
    reverseString(input) == input
  }

  def main(args: Array[String]): Unit = {
    println("Please enter a string and press enter")
    var userInput = readLine()

    var reversedStr = reverseString(userInput)
    var isPalindrome = isPalindrom(userInput)
    println(f"$userInput%s a palindrom ? $isPalindrome%s")
  }
}
