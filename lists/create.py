if __name__ == '__main__':
    seq_ls = {1: 446, 2:232, 6:269, 18:338, 20:836}
    res = []
    for seq in [1, 2, 6, 18, 20]:
        for scene in ['15-deg-left', '15-deg-right', '30-deg-left', '30-deg-right', 'clone']:
            for frame in range(seq_ls[seq]):
                img1 = 'vkitti_1.3.1_rgb/%04d/%s/%05d.png'%(seq, scene, frame)
                img2 = 'vkitti_1.3.1_rgb/%04d/%s/%05d.png'%(seq, scene, frame+1)
                flow = 'vkitti_1.3.1_flowgt/%04d/%s/%05d.png'%(seq, scene, frame)
                res += ['%s %s %s\n'%(img1, img2, flow)]

    with open('t.txt', 'w') as f:
        f.writelines(res)