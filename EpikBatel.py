using System;
using System.IO;

namespace EpicBattle
{
    class Program
    {
        static void Main(string[] args)
        {
            //string[] heroes = {"Harry Potter", "SuperMan", "Luke Skywalker", "Lara Croft"};
            //string[] villains = {"Voldemort", "Joker", "Venom", "Darth Vader", "Cruella"};
            string folderPath = @"C:\Users\opilane\Samples\";
            string[] heroes = GetDataFromFile(folderPath + "heroes.txt");
            string[] villains = GetDataFromFile(folderPath + "villains.txt");
            string[] heroesweapon = GetDataFromFile(folderPath + "heroesweapon.txt");
            string[] villainsweapon = GetDataFromFile(folderPath + "villainsweapon.txt");
            string[] armor = GetDataFromFile(folderPath + "armor.txt");

            string randomHero = GetRandomElement(heroes);
            string randomvillain = GetRandomElement(villains);

            string Hweapon = GetRandomElement(heroesweapon);
            string Vweapon = GetRandomElement(villainsweapon);

            string heroarmor = GetRandomElement(armor);
            string villainarmor = GetRandomElement(armor);



            int heroHP = GenerateHP(heroarmor);
            int villainHP = GenerateHP(villainarmor);

            Console.WriteLine($"Your random  hero is: {randomHero} in {heroarmor}");
            Console.WriteLine($"Your random  villains is: {randomvillain} in {villainarmor}");
            Console.WriteLine($"{randomHero} with {Hweapon} will fight {randomvillain} with {Vweapon}");
            Console.WriteLine($"{randomvillain} HP: {villainHP}");
            Console.WriteLine($"{randomHero} HP: {heroHP}");

            while (heroHP >= 0 && villainHP >= 0)
            {
                heroHP = heroHP - Hit(randomvillain, Vweapon);
                villainHP = villainHP - Hit(randomHero, Hweapon);
            }
            if (heroHP > villainHP)
            {
                Console.WriteLine($"{randomHero} saves the day!");
            }
            else if (heroHP < villainHP)
            {
                Console.WriteLine("Dark side wins!");
            }
            else
            {
                Console.WriteLine($"Someday {randomHero} shall fight {randomvillain} again!");
            }
        }

        public static string GetRandomElement(string[] someArray)
        {
            Random rnd = new Random();
            int randomIndex = rnd.Next(0, someArray.Length);
            string randomCharacter = someArray[randomIndex];
            return randomCharacter;
        }

        public static string[] GetDataFromFile(string filepath)
        {
            string[] datafromfile = File.ReadAllLines(filepath);
            return datafromfile;
        }

        public static int GenerateHP(string armor)
        {
            int CharacterHP = armor.Length;
            return CharacterHP;

        }

        public static int Hit(string character, string weapon)
        {
            Random rnd = new Random();
            int strike = rnd.Next(0, weapon.Length - 2);
            Console.WriteLine($"{character} hit {strike}!");

            if (strike == weapon.Length - 2)
            {
                Console.WriteLine($"Awesome! {character} made a critical hit!");
            }
            else if (strike == 0)
            {
                Console.WriteLine($"Bad luck! {character} missed the target!");
            }

            return strike;
        }
    }
}

    

    
