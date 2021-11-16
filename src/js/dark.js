function toggleDark() {
  if (document.getElementById("content").classList.contains('light-mode')){
    document.getElementById("content").classList.toggle('light-mode');
    document.getElementById("svg").classList.add('svg-dark');
    document.getElementById("svg").classList.remove('svg-light');
    document.getElementById("switch").classList.add('svg-dark');
    document.getElementById("switch").classList.remove('svg-light');
    document.getElementById("main").classList.add('clr-light');
    document.getElementById("main").classList.remove('clr-dark');
    document.getElementById("foo").classList.add('clr-light');
    document.getElementById("foo").classList.remove('clr-dark');
    document.getElementById("switch").src="images/lightmode.svg";
  } else {
    document.getElementById("content").classList.toggle('light-mode')
    document.getElementById("svg").classList.add('svg-light');
    document.getElementById("svg").classList.remove('svg-dark');
    document.getElementById("switch").classList.add('svg-light');
    document.getElementById("switch").classList.remove('svg-dark');
    document.getElementById("main").classList.add('clr-dark');
    document.getElementById("main").classList.remove('clr-light');
    document.getElementById("foo").classList.add('clr-dark');
    document.getElementById("foo").classList.remove('clr-light');
    document.getElementById("switch").src="images/darkmode.svg";
  }
}
