public class Selection_sort {
    static void seeLc(int[] arr){
        for (int i = 0;i<arr.length;i++){
            int  min= i;
            for (int j = i;j < arr.length;j++){
                if(arr[j] < arr[min]){
                    min = j;
                }
            }
            if(min != i){
                int temp = arr[min];
                arr[min] = arr[i];
                arr[i] = temp;
            }
        }
        pin(arr);
    }
    static void pin(int[] arr){
        for (int i = 0;i < arr.length;i++){
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] arr={8,6,34,22,40,5,11,23,44,18};
        seeLc(arr);
    }
}
