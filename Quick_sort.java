public class Quick_sort {
    public static int sort(int arr[], int begin,int end){
        int i = begin-1;
        int j = begin;
        int poi = arr[end];
        while (j < end){
            if(arr[j] < poi){
                i++;
                swap(arr,i,j);
            }
            j++;
        }
        swap(arr,i+1,end);
        return i+1;
    }
    public static void swap(int arr[],int a,int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    public static void in(int arr[]){
        for (int i=0;i<arr.length;i++){
            System.out.print(arr[i]);
        }
        System.out.println();

    }
    public static void Quick(int[] arr ,int begin,int end){
        if(begin >= end){
            return;
        }
        else{
            int poIn = sort(arr, begin, end);
            in(arr);
            Quick(arr,begin,poIn-1);
            Quick(arr,poIn+1,end);
        }
    }
    public static void main(String[] args) {
        int [] arr = {1, 3, 9, 8, 2, 7, 5};
        Quick(arr,0,arr.length-1);
    }
}
