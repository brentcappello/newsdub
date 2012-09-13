function updateslug(){
    title = document.getElementById("id_title").value;
//        title = title.replace(/\s+/g, '-').toLowerCase();
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for", "from",
    "is", "in", "into", "like", "of", "off", "on", "onto", "per",
    "since", "than", "the", "this", "that", "to", "up", "via",
    "with"];
    r = new RegExp('\\b(' + removelist.join('|') + ')\\b', 'gi');
    title = title.replace(r, '');
    // if downcode doesn't hit, the char will be stripped here
    title = title.replace(/[^-\w\s]/g, ''); // remove unneeded chars
    title = title.replace(/^\s+|\s+$/g, ''); // trim leading/trailing spaces
    title = title.replace(/[-\s]+/g, '-'); // convert spaces to hyphens
    title = title.toLowerCase(); // convert to lowercase
    document.getElementById("id_slug").value = title;
    }
//This piece of JS was for forked from urlify.js this needs to be in static or fixtures