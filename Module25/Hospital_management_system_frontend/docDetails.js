const getparams = () => {
  const param = new URLSearchParams(window.location.search).get("doctorId");
  loadTime(param);
  fetch(`https://testing-8az5.onrender.com/doctor/list/${param ? param : ""}`)
    .then((res) => res.json())
    .then((data) => displayDetails(data));

  fetch(
    `https://testing-8az5.onrender.com/doctor/review/?doctor_id=${
      param ? param : ""    }`
  )
    .then((res) => res.json())
    .then((data) => doctorReview(data));
};

const doctorReview = (reviews) => {
  reviews.forEach((review) => {
    const parent = document.getElementById("doc-details-review");
    const div = document.createElement("div");
    div.classList.add("review-card");
    div.innerHTML = `
            <img src="./Images/girl.png" alt="" />
            <h4>${review.reviewer}</h4>
            <p>
              ${review.body.slice(0, 100)}
            </p>
            <h6>${review.rating}</h6>
    `;
    parent.appendChild(div);
  });
};

const displayDetails = (doctor) => {
  const parent = document.getElementById("doc-details");
  const div = document.createElement("div");
  div.classList.add("doc-details-container");
  div.innerHTML = `
      <div class="doctor-img">
            <img src=${doctor.image} alt="">
        </div>
        <div class="doc-info">
            <h1>${doctor.full_name}</h1>
            ${doctor.specialization
              .map((item) => {
                return `<button class="doc-details-btn">${item}</button>`;
              })
              .join(" ")}
            ${doctor.designation
              .map((item) => {
                return `<h4 >${item}</h4>`;
              })
              .join(" ")}
            <p class="w-50">Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse, ad! Lorem ipsum dolor sit, amet consectetur adipisicing elit. Hic, repellat?</p>
            <h4>Fees: ${doctor.fee}BDT</h4>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
                 Take Appointment
            </button>
        </div>
    `;
  parent.appendChild(div);
};

const loadTime = (id) => {
  fetch(
    `https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`
  )
    .then((res) => res.json())
    .then((data) => {
      data.forEach((item) => {
        const parent = document.getElementById("time-container");
        const option = document.createElement("option");
        option.value = item.id;
        option.innerText = item.name;
        parent.appendChild(option);
      });
      console.log(data);
    });
};

const handleAppointment = () => {
  console.log("Hello");
  const param = new URLSearchParams(window.location.search).get("doctorId");

  const status = document.getElementsByName("status");
  const selected = Array.from(status).find((button) => button.checked);
  // console.log(selected);
  const symptom = document.getElementById("symptom").value;
  const time = document.getElementById("time-container");
  const selectedTime = time.options[time.selectedIndex];
  // console.log(symptom,selectedTime);
  const info = {
    appointment_type: selected.value,
    appointment_status: "Pending",
    time: selectedTime.value,
    symptom: symptom,
    cancle: false,
    patient: 1,
    doctor: param,
  };
 console.log(info);
  fetch(`https://testing-8az5.onrender.com/appointment/`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify(info),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
    });
};
getparams();
