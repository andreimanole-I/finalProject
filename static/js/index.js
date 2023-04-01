const progress = document.querySelector('.progress')
        const percentage = document.querySelector('.progress span')

        let per = 0;
        function progressLoad(){
            if(per>=20){
                progress.style.width = `20%`;
                percentage.innerHTML = "20%"

            }else{
                progress.style.width = `${per}%`;
                percentage.innerHTML = `${per}%`;

            }
            per++

        }

        setInterval(progressLoad,30)