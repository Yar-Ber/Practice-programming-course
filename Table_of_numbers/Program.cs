Console.Write("Enter the number of columns: ");
if (int.TryParse(Console.ReadLine(), out int columns)) //reading column count from console input

if (columns <= 0) //checking the correctness of the number of columns
{
    Console.WriteLine("The number of columns you entered is incorrect");
    return;
}

Console.Write("Enter the number of rows: ");
if (int.TryParse(Console.ReadLine(), out int rows)) //reading row count from console input

if (rows <= 0) //checking the correctness of the number of rows
{
    Console.WriteLine("The number of rows you entered is incorrect");
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

