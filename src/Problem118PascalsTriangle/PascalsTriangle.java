package Problem118PascalsTriangle;

import java.util.ArrayList;
import java.util.List;

public class PascalsTriangle {
    public static List<List<Integer>> generate(int numRows) {
        List<List<Integer>> listOfLists = new ArrayList<>();
        for (int outIdx = 0; outIdx < numRows; outIdx++) {
            listOfLists.add(new ArrayList<Integer>());
            for (int inIdx = 0; inIdx <= outIdx; inIdx++) {

                if (inIdx == 0 || inIdx == outIdx) {
                    listOfLists.get(outIdx).add(1);
                }
                else {
                    List<Integer> innerList =  listOfLists.get(outIdx-1);
                    int valueAtOutIdxInIdx = innerList.get(inIdx - 1) + innerList.get(inIdx);
                    listOfLists.get(outIdx).add(valueAtOutIdxInIdx);
                }

            }
        }
        return listOfLists;
    }

    public static void printList(List<List<Integer>> listOfLists) {
        StringBuilder sb = new StringBuilder("[");
        for (List<Integer> list : listOfLists) {
            sb.append(list.toString());
            sb.append(", ");
        }
        if (listOfLists.size() > 0) {
            sb.setLength(sb.length() - 2);  // Remove the trailing ", "
        }
        sb.append("]");
        System.out.println(sb.toString());
    }

    public static void main(String[] args) {
        printList(generate(5));
        printList(generate(1));
    }
}
