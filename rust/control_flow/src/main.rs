fn main() {
  println!("Hello, world!");

  // Basic Branch
  let number = 8;
  if number < 5 {
    println!("lower then 5");
  } else {
    println!("greater then 5");
  }

  // If statements are expressions, they evaluate to something!
  let number2 = if true {
    println!("top");
    "top"
  } else {
    "bottom"
  };
  println!("{}", number2);

  // loop forever
  // loop {
  //   println!("looooop");
  // }

  // loop returns break expression
  let mut counter = 0;

  let result = loop {
    counter += 1;

    if counter == 23 {
      break counter * 4;
    }
  };

  println!("{}", result);

  let mut number = 3;
  while number != 0 {
    println!("{}!", number);

    number -= 1;
  }
  println!("LIFTOFF!!!");

  // Loop over array
  let a = [10, 20, 30, 40, 50];
  let mut index = 0;

  while index < 5 {
    println!("the value is: {}", a[index]);

    index += 1;
  }

  for element in a.iter() {
    println!("the value is: {}", element);
  }

  for number in (1..4).rev() {
    println!("{}!", number);
  }
  println!("LIFTOFF!!!");
}
