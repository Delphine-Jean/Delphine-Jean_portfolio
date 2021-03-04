object Exercise3 {
  def findTheRichest(bank:Map[String,Double]): String = {
    bank.toList.maxBy(_._2)._1
  }
  def mergeBanks(firstCurrency:String,
                firstBank:Map[String,Double],
                secondCurrency:String,
                secondBank: Map[String, Double]): Map[String,Map[String, Double]] = {
    val updatedFirstBank = firstBank.map(x => x).transform((key,value) => (firstCurrency, value))
    val updatedSecondBank = secondBank.map(x => x).transform((key,value) => (secondCurrency,value))

    (updatedFirstBank.toSeq ++ updatedSecondBank.toSeq)
      .groupBy(_._1)
      .transform((key,value) => value.map(x=>x._2).toMap)
  }


  def main(args: Array[String]): Unit = {
    val bankInEuros = Map("Paul" -> 10.0, "Antoine" -> 20.0, "Charles" -> 5.0)
    val bankInDollars = Map("Paul" -> 100.0, "Antoine" -> 5.0, "Charles" -> 50.0)

    println(findTheRichest(bankInEuros))
    println(findTheRichest(bankInDollars))
    println(mergeBanks("$", bankInDollars, "â‚¬", bankInEuros))
  }
  }
