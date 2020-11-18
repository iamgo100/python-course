def render_list(seq):
    seq_render = []
    if seq:
        for i in range(len(seq)):
            seq_render.append(f'<li><span class="name">{seq[i]["name"]}</span><span class="message">{seq[i]["message"]}</span></li>')
    return ''.join(seq_render)