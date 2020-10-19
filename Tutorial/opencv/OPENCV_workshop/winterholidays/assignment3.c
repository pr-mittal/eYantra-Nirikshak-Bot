#include<stdio.h>
#include<stdlib.h>
//make strcpy
//make strcmp
void strcpy(char s1[],char s2[])
{
    int i=0;
    while(s1[i]!=0)
    {
        s2[i]=s1[i];
        i++;
    }
    s2[i]='\0';
}
int strlen(char s[])
{
    int i=0;
    while(s[i]!='\0')
    {
        i++;
    }
    return i;

}
int strcmp(char s1[],char s2[])
{
    int i=0;
    while(s1[i]!='\0')
    {

        if(s1[i]!=s2[i])
            break;
        i++;
    }
    if(i==strlen(s1))
        return 1;
    return 0;
}
struct newNode{
char data[10];
char key[5];
struct newNode *next;
};
//insert a node at the head and update the head
void insertNode(struct newNode **head_ref)
{
        struct newNode *node=(struct newNode *)malloc(sizeof(struct newNode));
        node->next=*head_ref;
        *head_ref=node;


}
//delete a node at the head and update the head
void deleteNode(struct newNode **head_ref)
{
    struct newNode * temp=(struct newNode*)malloc(sizeof(struct newNode));
    //temp is used to point at the head and delete that node
    temp=*head_ref;
    *head_ref=temp->next;
    free(temp);

}
void DISPLAY(struct newNode **head_ref)
{
    struct newNode *temp=(struct newNode*)malloc(sizeof(struct newNode));
    //place temp pointer at the head
    temp=*head_ref;
    //list has only one element
    if(temp->next==0)
    {
        printf("No elemeNT TO DISPLAY\n");
        return;
    }
    //go to the last node
    struct newNode *print=(struct newNode*)malloc(sizeof(struct newNode));
    print->next=NULL;
    while(temp->next!=NULL)
    {
        //pushing the elements to a list for printing afterwards
        //head is empty as new node is added every time we add an element
        temp=temp->next;
        strcpy(temp->data,print->data);
        insertNode(&print);

    }
    //reached the last node
    //head is empty as new node is added every time we add an element
    while(print->next!=NULL)
    {
        print=print->next;
        printf("%s ",print->data);
        //printf("2");

    }
    printf("\n");

}
//make DEL
int DEL(struct newNode **head_ref)
{
    struct newNode *temp=*head_ref,*prev;
    //change head if head element is deleted
    //list has only one element
    if(temp->next==NULL)
    {
        printf("No elemet was added\n");
        return;
    }
    /*else if(strcmp(temp->key,"P"))
    {
        //head is to be deleted
        *head_ref=temp->next;
        free(temp);


    }
    */
               //since head element is empty as no new element is added on every ADD
            temp=temp->next;
            //changing head until at least one NP comes starting fro head
            while(strcmp(temp->key,"P")&&(temp->next!=NULL))
            {
                (*head_ref)->next=temp->next;
                free(temp);
                temp=temp->next;

            }
            //storing address of previous element for later use
            prev=temp;
    while(temp->next!=NULL)
        {



            if(strcmp(temp->key,"P"))
            {
                prev->next=temp->next;
                free(temp);
            }
            else
            {
                prev=temp;
            }
            temp=temp->next;

        }
        //working on last element
        if(strcmp(temp->key,"P"))
            {
                prev->next=NULL;
                free(temp);
            }
    //printf("deleted\n");



}
//write for overflow and underflow
int main()
{
    //declaring list
    struct newNode* head=(struct newNode*)malloc(sizeof(struct newNode));
    head->next=NULL;
    int n,m,i;
    scanf("%d",&n);
    scanf("%d",&m);
    char a[10],b[10],c[2];
    for(i=0;i<m;i++)
    {
        scanf("%s",a);
        if(strcmp(a,"ADD"))
        {
            scanf("%s",head->data);
            scanf("%s",head->key);
            /*
            if(head==0)
            {
                struct newNode* head=(struct newNode*)malloc(sizeof(struct newNode));
                head->next=NULL;
            }
            */
            insertNode(&head);
        }
        else if(strcmp(a,"DEL"))
        {
            DEL(&head);
        }
        else if(strcmp(a,"DISPLAY"))
        {
            DISPLAY(&head);

        }
    }
    printf("end");


}
