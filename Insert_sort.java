public class Main {
    public static void sortInsert(int [] arr){
        for (int i = 0 ;i < arr.length-1;i++){
            int pot = arr[i+1];
            for (int j = i;j > -1;j--){
                if(arr[j] > pot){
                    arr[j+1] = arr[j];
                    if(pot < arr[j] && j==0){
                        arr[0]=pot;

                    }
                }
                else {
                    arr[j+1] = pot;
                    break;
                }
            }
            in(arr);
        }
    }
    public static void in(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.println();

    }
    public static void main(String[] args) {
        int[] arr = {1, 4, 3, 5, 6, 2};
        sortInsert(arr);

    }
}
