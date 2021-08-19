class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> myset;
        bool isPresent = false;
        for(auto i: wordList){
            if(i == endWord)
                isPresent = true;
            myset.insert(i);
        }
        if(isPresent == false)
            return 0;
        
        queue<string> q;
        q.push(beginWord);
        int depth = 0;
        
        
        while(!q.empty()){
            int k = q.size();
            depth += 1;
            while(k > 0){
                string word = q.front();
                q.pop();
                for(int i=0; i<word.length(); i++){
                    string temp = word;
                    for(char j = 'a'; j<='z'; j++){
                        temp[i] = j;
                        if(temp == word)
                            continue;
                        if(temp == endWord)
                            return depth+1;
                        if(myset.find(temp) != myset.end()){
                            q.push(temp);
                            myset.erase(temp);
                        }
                    }
                    
                }
                k --;
            }
            
        }
        
        return 0;
    }
};
