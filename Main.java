package com.company;

import java.util.Scanner;

public class Main {
    static class SinglyLinkedListNode{
        public int data ;
        public SinglyLinkedListNode next;
        public SinglyLinkedListNode(int nodeData){
            this.data = nodeData;
            this.next = null;
        }
    }
    static class SinglyLinkedList{
        public SinglyLinkedListNode head;
        public SinglyLinkedListNode tail;
        public SinglyLinkedList(){
            this.head = null;
            this.tail = null;
        }
        public void insertNode(int nodeData){
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);
            if(this.head==null){
                this.head=node;
            }
            else{
                this.tail.next = node;
            }
            this.tail=node;
        }

    }
    // in danh sách liên kết
    public static void print(SinglyLinkedListNode head){
        SinglyLinkedListNode node = head;
        while (node!=null){
            System.out.println(node.data);
            node=node.next;
        }
    }

    public static void main(String[] args) {
	// write your code here
        SinglyLinkedList list = new SinglyLinkedList();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i= 0;i<n;i++){
            list.insertNode(scanner.nextInt());
        }
        print(list.head);
    }
}
