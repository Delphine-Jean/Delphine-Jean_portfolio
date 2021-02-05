object Exercise2 {
def filterList(inputList: List[String], beginWith: String, maxlength: Int) : List[String] = {
  inputList
    .filter(str => str.startsWith((beginWith)))
    .filter(str => str.length <= maxlength)
}

  def main(args: Array[String]): Unit = {
    val list = List("penguin", "pentagon","shape","pen","shopping","pent","shinning")

    println(filterList(list,"pen",4))
    println(filterList(list,"pen",10))
    println(filterList(list,"sh",10))
  }
}
