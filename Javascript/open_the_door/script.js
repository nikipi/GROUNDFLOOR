//Get Door Image from HTML, Get Start button from HTML
let doorImage1 = document.getElementById('door1');
let doorImage2 = document.getElementById('door2');
let doorImage3 = document.getElementById('door3');
let startButton = document.getElementById('start');

// Door paths
let botDoorPath ='https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/robot.svg';

let closedDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/closed_door.svg';

let beachDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/beach.svg';

let spaceDoorPath = 'https://s3.amazonaws.com/codecademy-content/projects/chore-door/images/space.svg';

let openDoor1;
let openDoor2;
let openDoor3;

let currentlyPlaying = true;

const isBot = door => {
 if(door.src === botDoorPath) {
     return true;
    } else {
     return false;
    }  
};

//Check if door is open
const isClicked = (door) => {
  if (door.src===closedDoorPath) {
    return false;
  } else {
    return true;
  }
}

//Decrease the amount if a door is opened
const playDoor = door => {
  numClosedDoors--;
  if(numClosedDoors === 0) {
      gameOver('win');
  } else if(isBot(door)) {
     gameOver();
  }
};


//Random picture under door function
const randomChoreDoorGenerator = () => {
  let numClosedDoors = 3;
  let choreDoor = Math.floor(Math.random()*numClosedDoors);

  /*   create ramdom integer */
  if (choreDoor === 0) {
    openDoor1 = botDoorPath;
    openDoor2 = beachDoorPath;
    openDoor3 = spaceDoorPath;
  }
  else if (choreDoor === 1) {
    openDoor2 = botDoorPath;
    openDoor3 = beachDoorPath;
    openDoor1 = spaceDoorPath;
  }
  else if (choreDoor === 2) {
    openDoor3 = botDoorPath;
    openDoor1 = beachDoorPath;
    openDoor2 = spaceDoorPath;
  }
}

/*  remember this syntax */
door1.onclick = () => {
  //doorImage3.src = botDoorPath;
    if (!isClicked(doorImage1) && currentlyPlaying) {
      doorImage1.src = openDoor1;
      playDoor(door1);
      }
};

door2.onclick = () => {
  //doorImage3.src = beachDoorPath;
    if (!isClicked(doorImage2) && currentlyPlaying) {
      doorImage2.src = openDoor2;
      playDoor(door2);
      }
};

door3.onclick = () => {
  //doorImage3.src = spaceDoorPath;
    if (!isClicked(doorImage3) && currentlyPlaying) {
      doorImage3.src = openDoor3;
      playDoor(door3);
      }
};

const startRound = () => {
  doorImage1.src = closedDoorPath;
  doorImage2.src = closedDoorPath;
  doorImage3.src = closedDoorPath;
  numClosedDoors = 3;
  startButton.innerHTML = 'Good Luck';
  currentlyPlaying = true;
  randomChoreDoorGenerator();
}

startButton.onclick = () => {
  if (currentlyPlaying === false) {
      startRound(); 
  }
  };

//Game over area
const gameOver = status => {
   if(status === 'win') {
     startButton.innerHTML = 'You win! Play again?';
   } else {
     startButton.innerHTML = 'Game over! Play again?';
   }
   currentlyPlaying = false;
   }; 

startRound();