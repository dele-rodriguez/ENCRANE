        // Declare Variables
        const pagination_btns = document.querySelectorAll(".pagination button"),
                count_answered = document.querySelector("#count-answered"),
                total_questions = document.querySelector("#total-questions")
                const unit_questions = document.querySelectorAll(".unit-question"),
                submit = document.querySelector("#submit")

        total_questions.innerText = unit_questions.length



        /*Number of answered questions*/
        let count_checked = setInterval(() => {
            let checked_radios = document.querySelectorAll("input[type='radio']:checked")
            answered_questions = checked_radios.length
            count_answered.innerText = answered_questions
        }, 1000);



        /*Pagination*/
        const pagination_numbers = document.querySelector(".pagination")
        const paginatedList = document.querySelector("form");
        const prev = document.querySelector("#prev")
        const next = document.querySelector("#next")

        const paginationLimit = 1;
        const pageCount = Math.ceil(unit_questions.length / paginationLimit);
        let currentPage;

        const appendPageNumber = (index) => {
        const pageNumber = document.createElement("button");
        pageNumber.className = "pagination-number";
        pageNumber.innerHTML = index;
        pageNumber.setAttribute("page-index", index);
        pageNumber.setAttribute("aria-label", "Page " + index);
        pagination_numbers.appendChild(pageNumber);
        };
        const getPaginationNumbers = () => {
        for (let i = 1; i <= pageCount; i++) {
            appendPageNumber(i);
        }
        };


        const setCurrentPage = (pageNum) => {
            currentPage = pageNum;

            handleActivePageNumber();
            handlePageButtonsStatus();
            const prevRange = (pageNum - 1) * paginationLimit;
            const currRange = pageNum * paginationLimit;
            unit_questions.forEach((item, index) => {
                item.classList.add("hidden");
                if (index >= prevRange && index < currRange) {
                item.classList.remove("hidden");
                }
            });
        };
        window.addEventListener("load", () => {
        getPaginationNumbers();
        setCurrentPage(1);

        prev.addEventListener("click", () => {
            setCurrentPage(currentPage - 1);
        });
        next.addEventListener("click", () => {
            setCurrentPage(currentPage + 1);
        });

        document.querySelectorAll(".pagination-number").forEach((button) => {
            const pageIndex = Number(button.getAttribute("page-index"));
            if (pageIndex) {
            button.addEventListener("click", () => {
                setCurrentPage(pageIndex);
            });
            }
        });
        });

        const disableButton = (button) => {
        button.classList.add("disabled");
        button.setAttribute("disabled", true);
        };
        const enableButton = (button) => {
        button.classList.remove("disabled");
        button.removeAttribute("disabled");
        };
        const handlePageButtonsStatus = () => {
        if (currentPage === 1) {
            disableButton(prev);
        } else {
            enableButton(prev);
        }
        if (pageCount === currentPage) {
            disableButton(next);
        } else {
            enableButton(next);
        }
        };
        const handleActivePageNumber = () => {
        document.querySelectorAll(".pagination-number").forEach((button) => {
            button.classList.remove("active");

            const pageIndex = Number(button.getAttribute("page-index"));
            if (pageIndex == currentPage) {
            button.classList.add("active");
            }
        });
        };



        /*Count down*/

        // Set the countdown time in minutes
        

        // Get the countdown element from the HTML
        var countdownElement = document.querySelector(".time-left");

        // Set an interval to update the countdown every second
        var countdownInterval = setInterval(function() {
        // Convert the countdown time to hours and minutes
        var hours = Math.floor(countdownTime / 60);
        var minutes = countdownTime % 60;

        // Format the countdown display
        var countdownDisplay = hours.toString().padStart(2, "0") + " : " + minutes.toString().padStart(2, "0");

        // Update the countdown element with the display text
        countdownElement.innerHTML = countdownDisplay;

        // Decrease the countdown time by 1 minute
        countdownTime--;

        // Stop the countdown when it reaches 0
        if (countdownTime < 0) {
            clearInterval(countdownInterval);
            countdownElement.innerHTML = "00 : 00";
            document.querySelector("#hide_submit").click()
        }
        }, 1000);

        submit.addEventListener("click", function(e){

            if (confirm("Are you sure you want to submit?")) {

                e.disabled = true
                } else {
                    e.preventDefault()
                }
            })

        const radios = document.querySelectorAll("input[type='radio']")
        for (var i = 0; i< radios.length; i++){
            if (i % 4 == 0){
                var groupId = Math.floor(i / 4)
            }
            radios[i].setAttribute("onclick", "check("+ groupId +")")
        }

        /*answered questions*/

        function check(num){
            document.querySelectorAll(".pagination-number")[num].classList.add("answered")
        }