using System;

class Day1 {
  static void Main() {
    string data = System.IO.File.ReadAllText(@"day1.input").Trim();
    int[] ilist = new int[data.Length];
    for (int i=0; i<data.Length; i++) {
        int idata = (int)Char.GetNumericValue(data[i]);
        ilist[i] = idata;
    }

    int sum = 0;
    for(int i=0; i<ilist.Length; i++) {
        if (ilist[i] == ilist[(i+1)%ilist.Length]) {
            sum += ilist[i];
        }
    }
    Console.WriteLine("part 1 {0}", sum);

    sum = 0;
    int halflen = ilist.Length / 2;
    for(int i=0; i<ilist.Length; i++) {
        if (ilist[i] == ilist[(i+halflen)%ilist.Length]) {
            sum += ilist[i];
        }
    }
    Console.WriteLine("part 2 {0}", sum);

  }
}