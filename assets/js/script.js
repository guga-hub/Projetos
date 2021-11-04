document.querySelector('.open-menu').addEventListener('click', e => {

    console.log('click');

    document.querySelector('header .menu').classList.add('open');

});

document.querySelector('.close-menu button').addEventListener('click', e => {

    console.log('click');

    document.querySelector('header .menu').classList.remove('open');

});

document.querySelector('.menu .backdrop').addEventListener('click', e => {

    console.log('click');

    document.querySelector('header .menu').classList.remove('open');

});