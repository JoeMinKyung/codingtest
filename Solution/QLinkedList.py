class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class BrowserHistory(object):
    def __init__(self, homepage):
       self.head=self.current=ListNode(val=homepage)
    def visit(self, url):
        self.current.next=ListNode(val=url,prev=self.current)
        self.current=self.current.next
        return None
    def back(self, steps):
        while steps>0 and self.current.prev!=None:
            steps-=1
            self.current=self.current.prev
        return self.current.val
    def forward(self, steps):
        while steps>0 and self.current.next!=None:
            steps-=1
            self.current=self.current.next
        return self.current.val
        

browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
print(browserHistory.visit("linkdein.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))

# None
# None
# None
# None
# "facebook.com"
# "google.com"
# "facebook.com"
# None
# "linkedin.com"
# "google.com"
# "leetcode.com"