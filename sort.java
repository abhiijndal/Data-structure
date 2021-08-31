

class Sorting{
    public void arr(int arr[]){
        int n=arr.length;;
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n-i-1;j++){
                if(arr[i]> arr[j+1]){
                    int Temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=Temp;

                }


            }
            
        }
        
    }
    
    public void printarr(int  arr[]){
        int n=arr.length;
        for(int i=0;i<n;i++){
            System.out.println(arr[i]+" ");


        }
    }

}
public class sort {
    public static void main(String[] args) {
        Sorting s=new Sorting();
        int arr[]={32,42,442,323,424,33,4,53,322,30,3};
        s.arr(arr);
        System.out.print("sorted array:");
        s.printarr(arr);

    }

        
    
    
}
