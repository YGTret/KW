import java.util.ArrayList;
import java.util.Scanner;

// Класс для животных
class Animal {
    String name;
    @SuppressWarnings("unused")
    private String type;
    private ArrayList<String> commands;

    public Animal(String name, String type) {
        this.name = name;
        this.type = type;
        this.commands = new ArrayList<>();
    }

    public void addCommand(String command) {
        commands.add(command);
    }

    public void displayCommands() {
        System.out.println("Список команд для животного " + name + ":");
        for (String command : commands) {
            System.out.println(command);
        }
    }
}

// Класс для счетчика
class Counter implements AutoCloseable {
    private int count;

    public Counter() {
        this.count = 0;
    }

    public void add() {
        count++;
    }

    public int getCount() {
        return count;
    }

    @Override
    public void close() {
        // Проверяем, что счетчик был использован в ресурсном блоке try-with-resources
        if (count == 0) {
            throw new IllegalStateException("Счетчик не был использован в ресурсном блоке try-with-resources");
        }
    }
}

public class AnimalRegistry {
    public static void main(String[] args) {
        try (Counter counter = new Counter()) { // Используем счетчик в блоке try-with-resources
            try (Scanner scanner = new Scanner(System.in)) {
                ArrayList<Animal> animals = new ArrayList<>();

                boolean running = true;
                while (running) {
                    System.out.println("\nМеню:");
                    System.out.println("1. Завести новое животное");
                    System.out.println("2. Определить животное в правильный класс");
                    System.out.println("3. Увидеть список команд, которое выполняет животное");
                    System.out.println("4. Обучить животное новым командам");
                    System.out.println("5. Выйти");

                    System.out.print("Выберите действие: ");
                    int choice = scanner.nextInt();
                    scanner.nextLine(); // Считываем оставшийся символ новой строки

                    switch (choice) {
                        case 1:
                            System.out.print("Введите имя животного: ");
                            String name = scanner.nextLine();
                            System.out.print("Введите тип животного: ");
                            String type = scanner.nextLine();
                            animals.add(new Animal(name, type));
                            counter.add(); // Увеличиваем значение счетчика при добавлении нового животного
                            System.out.println("Животное успешно добавлено!");
                            break;
                        case 2:
                            // Реализация определения животного в правильный класс
                            break;
                        case 3:
                            System.out.print("Введите имя животного: ");
                            String animalName = scanner.nextLine();
                            for (Animal animal : animals) {
                                if (animal.name.equals(animalName)) {
                                    animal.displayCommands();
                                    break;
                                }
                            }
                            break;
                        case 4:
                            // Реализация обучения животного новым командам
                            break;
                        case 5:
                            running = false;
                            break;
                        default:
                            System.out.println("Некорректный выбор. Пожалуйста, выберите существующий пункт меню.");
                    }
                }
            }
        } catch (IllegalStateException e) {
            System.err.println("Ошибка: " + e.getMessage());
        }
    }
}
