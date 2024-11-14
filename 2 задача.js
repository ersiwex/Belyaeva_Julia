document.getElementById('reservationForm').addEventListener('submit', addReservation);

function addReservation(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const datetime = document.getElementById('datetime').value;
    const reservationList = document.getElementById('reservationList');

    const li = document.createElement('li');
    li.textContent = Name: ${name}, Email: ${email}, Date/Time: ${datetime};
    reservationList.appendChild(li);

    document.getElementById('reservationForm').reset();
}