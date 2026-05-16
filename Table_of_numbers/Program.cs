Console.Write("Enter the number of columns: ");
int columns;
if (int.TryParse(Console.ReadLine(), out columns)) //reading column count from console input

Console.Write("Enter the number of rows: ");
int rows;
if (int.TryParse(Console.ReadLine(), out rows)) //reading row count from console input

if (columns <= 0 || rows <= 0) //checking the correctness of the number of columns and rows
{
    Console.WriteLine("The number of columns/rows you entered is incorrect");
    return;
}

for (int i = 0; i < columns * rows; i++)    //iterate through each cell of the table by checking it
{
    Console.Write("{0, 5}", i); //the distance between the numbers in the table
    if ((i + 1) % columns == 0) //move to the next row
    {
        Console.WriteLine();
    }
} 

