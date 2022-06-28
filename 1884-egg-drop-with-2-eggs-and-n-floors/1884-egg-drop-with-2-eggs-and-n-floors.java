/*
2 identical eggs

floor x+1 - break
floor x=f - not break
floor x-1 - not break

move

reusing eggs if they dont break

asked: minimum numbers of moves to dertermine which value f is

approach:
    there are two iterators given (two eggs)
    split floors in a way, that it there is an optimal solution (i dont know the name of the algorithm... yet...)

*/

class Solution {
    public int twoEggDrop(int n) {
        int x=0;
        while(true){
            if (gauss(x) < n){
                x++;
            } else {
                return x;
            }
        }
    }
    
    private int gauss(int n){
        return n*(n+1)/2;
    }
}

