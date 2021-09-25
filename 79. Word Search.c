
bool check(char **board, int n,int m, int i, int j, char *word, int ch,int x){
    if(ch == x){
        return true;
    }
    if(i<0 || j<0 || i>=n || j>=m || word[ch]!=board[i][j]){
        return false;
    }
    
    char temp = board[i][j];
    board[i][j] = ' ';
    bool ans = check(board,n,m,i+1,j,word,ch+1,x) || check(board,n,m,i-1,j,word,ch+1,x) || check(board,n,m,i,j+1,word,ch+1,x) || check(board,n,m,i,j-1,word,ch+1,x);
    board[i][j] = temp;
    return ans;
}


bool exist(char** board, int boardSize, int* boardColSize, char * word){
    int i,j,x = strlen(word);
    for(i=0;i<boardSize;i++){
        for(j=0;j<(*boardColSize);j++){
            if (word[0] == board[i][j] && check(board,boardSize,*boardColSize,i,j,word,0,x)){
                return true;
            }
        }
    }
    return false;
}
