package com.company;

public class Main {
    static class SingLinkListNode{
        public int data;
        public SingLinkListNode next;
        public SingLinkListNode(int nodeData){
            this.data = nodeData;
            this.next = null;
        }
    }
    static class SingLinkList{
        public SingLinkListNode head;
        public SingLinkListNode tail;
        public SingLinkList(){
            this.head = null;
            this.tail = null;
        }
        public void insertNode(int nodeData){
            SingLinkListNode node = new SingLinkListNode(nodeData);
            if (this.head == null){
                this.head = node;
            }
            else {
                this.tail.next=node;
            }
            this.tail=node;
        }
    }
    public static void main(String[] args) {
	// write your code here
    }
}
